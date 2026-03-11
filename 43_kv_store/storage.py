# storage.py
import json
import threading
import time
from typing import Optional

def now(): return time.time()

class KVStore:
    def __init__(self, aof_path: Optional[str] = None):
        self.data = {}
        self.expiry = {}
        self.lock = threading.Lock()
        self.aof_path = aof_path
        if aof_path: open(aof_path, "a").close()

    def _persist(self, cmd):
        if not self.aof_path: return
        with open(self.aof_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(cmd)+"\n")

    def set(self, k, v, ttl=None):
        with self.lock:
            self.data[k] = v
            if ttl: self.expiry[k] = now()+ttl
            elif k in self.expiry: self.expiry.pop(k)
            self._persist(["SET", k, v, ttl])

    def get(self, k):
        with self.lock:
            if k in self.expiry and now() > self.expiry[k]:
                self.data.pop(k, None); self.expiry.pop(k, None); return None
            return self.data.get(k)

    def delete(self, k):
        with self.lock:
            self.data.pop(k, None); self.expiry.pop(k, None); self._persist(["DEL", k])
