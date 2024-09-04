#!/usr/bin/env python3
"""class FIFOCache module"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
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
            first_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Returns the value in `self.cache_data` linked to `key`."""
        return self.cache_data.get(key, None)
