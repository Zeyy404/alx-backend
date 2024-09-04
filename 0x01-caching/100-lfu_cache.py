#!/usr/bin/env python3
"""LFUCache module"""
from collections import defaultdict, OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Inherits from BaseCaching and implements LFU caching system"""
    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.cache_data = {}
        self.freq = defaultdict(int)
        self.order = defaultdict(OrderedDict)

    def _evict(self):
        """
        Evict the least frequently used item,
        or the least recently used among them.
        """
        min_freq = min(self.freq.values())
        lfu_items = self.order[min_freq]
        lru_key = next(iter(lfu_items))
        del self.cache_data[lru_key]
        del self.freq[lru_key]
        del self.order[min_freq][lru_key]
        if not self.order[min_freq]:
            del self.order[min_freq]
        print(f"DISCARD: {lru_key}")

    def put(self, key, item):
        """
        Assigns to the dictionary self.cache_data
        the `item` value for the key `key`.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self._update_frequency(key)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            self._evict()

        self.cache_data[key] = item
        self.freq[key] = 1
        self.order[1][key] = None

    def get(self, key):
        """Returns the value in `self.cache_data` linked to `key`."""
        if key is None or key not in self.cache_data:
            return None

        self._update_frequency(key)
        return self.cache_data[key]

    def _update_frequency(self, key):
        """Update frequency and ordering of the key"""
        freq = self.freq[key]
        del self.order[freq][key]
        if not self.order[freq]:
            del self.order[freq]

        self.freq[key] += 1
        new_freq = self.freq[key]

        if new_freq not in self.order:
            self.order[new_freq] = OrderedDict()
        self.order[new_freq][key] = None
