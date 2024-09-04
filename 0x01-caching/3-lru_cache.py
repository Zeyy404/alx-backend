#!/usr/bin/env python3
"""LRUCache module"""
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Inherits from BaseCaching and implements LRU caching system"""
    
    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.cache_data = OrderedDict()
    
    def put(self, key, item):
        """
        Assigns to the dictionary self.cache_data
        the `item` value for the key `key`.
        """
        if key is None or item is None:
            return
        
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {lru_key}")

        self.cache_data[key] = item

    def get(self, key):
        """Returns the value in `self.cache_data` linked to `key`."""
        if key is None or key not in self.cache_data:
            return None

        self.cache_data.move_to_end(key)
        return self.cache_data[key]
