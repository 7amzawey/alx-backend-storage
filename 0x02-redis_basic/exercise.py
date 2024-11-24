#!/usr/bin/env python3
"""Cache class."""
import uuid
import redis
from typing import Union


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
