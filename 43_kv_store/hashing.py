# hashing.py
import hashlib
from collections import OrderedDict

def hash_key(key: str) -> int:
    return int(hashlib.sha1(key.encode()).hexdigest(), 16)

class HashRing:
    def __init__(self, nodes, replicas=50):
        self.ring = OrderedDict(); self.sorted = []
        for n in nodes:
            for i in range(replicas):
                h = hash_key(f"{n}:{i}"); self.ring[h] = n
        self.sorted = sorted(self.ring)
    def get_node(self, key):
        h = hash_key(key)
        for k in self.sorted:
            if h <= k: return self.ring[k]
        return self.ring[self.sorted[0]]
