"""
Very simple LRU cache with optional TTL and a tiny CLI.

Commands (case-insensitive):
  PUT key value [ttl_seconds]
  GET key
  DELETE key
  CACHE      # show current items from most -> least recent
  EXIT
"""

from __future__ import annotations

import time
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.capacity = capacity
        self.store: OrderedDict[str, tuple[object, float | None]] = OrderedDict()

    def _expired(self, key: str) -> bool:
        value = self.store.get(key)
        if value is None:
            return False
        _, expiry = value
        return expiry is not None and time.time() > expiry

    def get(self, key: str):
        if key not in self.store or self._expired(key):
            self.store.pop(key, None)
            return None
        val, expiry = self.store.pop(key)
        self.store[key] = (val, expiry)  # move to end (MRU)
        return val

    def put(self, key: str, value, ttl: float | None = None):
        expiry = time.time() + ttl if ttl else None
        if key in self.store:
            self.store.pop(key)
        elif len(self.store) >= self.capacity:
            self.store.popitem(last=False)  # remove LRU
        self.store[key] = (value, expiry)

    def delete(self, key: str) -> bool:
        return self.store.pop(key, None) is not None

    def items(self):
        # return from MRU -> LRU
        for key in reversed(self.store):
            val, _ = self.store[key]
            yield key, val


def repl(cache: LRUCache):
    print("Simple LRU cache. Type EXIT to quit.")
    while True:
        try:
            line = input("> ").strip()
        except EOFError:
            break
        if not line:
            continue
        parts = line.split()
        cmd = parts[0].lower()

        if cmd == "put" and len(parts) >= 3:
            key, value = parts[1], parts[2]
            ttl = float(parts[3]) if len(parts) > 3 else None
            cache.put(key, value, ttl)
            print("OK")
        elif cmd == "get" and len(parts) >= 2:
            val = cache.get(parts[1])
            print("<nil>" if val is None else val)
        elif cmd == "delete" and len(parts) >= 2:
            print("REMOVED" if cache.delete(parts[1]) else "MISS")
        elif cmd == "cache":
            print(list(cache.items()))
        elif cmd == "exit":
            break
        else:
            print("Commands: PUT key val [ttl], GET key, DELETE key, CACHE, EXIT")


if __name__ == "__main__":
    cache = LRUCache(capacity=3)
    repl(cache)
