#!/usr/bin/env python3
"""Cache the page content."""
from functools import wraps
import redis
import requests


def cache_page(func):
    """Decorate the function."""
    r = redis.Redis(host='localhost', port=6379, db=0)

    @wraps(func)
    def wrapper(url) -> str:
        """Wrap the function."""
        count_key = f"count:{url}"
        cache_key = f"cache:{url}"
        r.incr(count_key)
        cached_page = r.get(cache_key)
        if cached_page:
            return cached_page.decode('utf-8')
        page_content = func(url)
        r.setex(cache_key, 10, page_content)
        return page_content
    return wrapper


@cache_page
def get_page(url: str) -> str:
    """Return a page html content."""
    return requests.get(url).text
