#!/usr/bin/env python3
"""class LIFOCache module"""
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """initailize the class"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Assigns to the dictionary self.cache_data
        the `item` value for the key `key`.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key, _ = self.cache_data.popitem(True)
            print(f"DISCARD: {last_key}")

        self.cache_data[key] = item

    def get(self, key):
        """Returns the value in `self.cache_data` linked to `key`."""
        return self.cache_data.get(key, None)
