#!/usr/bin/env python3
"""Cache class."""
import uuid
import redis
from functools import wraps
from typing import Callable, Optional, Union


def count_calls(method: Callable) -> Callable:
    """Return the count calls."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def replay(method):
    """Display the history of calls of a particular function."""
    redis_instance = method.__self__._redis
    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"

    inputs = redis_instance.lrange(input_key, 0, -1)
    outputs = redis_instance.lrange(output_key, 0, -1)

    print(f"{method.__qualname__} was called {len(inputs)} times:")
    for input_, output in zip(inputs, outputs):
        print(f"{method.__qualname__}(*{input_.decode('utf-8')}) -> "
              f"{output.decode('utf-8')}")


def call_history(method: Callable) -> Callable:
    """Call history decorator."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrap function."""
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))
        return result
    return wrapper


class Cache:
    """Cache class."""

    def __init__(self):
        """Store an instance of Redis client."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Return a string."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self, key: str,
            fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float, None]:
        """Get the value of the key."""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, bytes, int, float, None]:
        """Parametrize Cache.get with the correct conversion."""
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Union[str, bytes, int, float, None]:
        """Make an int out of the output."""
        return self.get(key, int)
