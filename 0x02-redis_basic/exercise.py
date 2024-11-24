#!/usr/bin/env python3
"""Cache class."""
import uuid
import redis
from typing import Callable, Optional, Union


class Cache:
    """Cache class."""

    def __init__(self):
        """Store an instance of Redis client."""
        self._redis = redis.Redis()
        self._redis.flushdb()

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
