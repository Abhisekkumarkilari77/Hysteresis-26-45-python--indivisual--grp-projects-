# models.py
import itertools

class Node:
    def __init__(self, name, cpu, mem):
        self.name = name; self.cpu = cpu; self.mem = mem
        self.used_cpu = 0; self.used_mem = 0; self.alive = True
        self.pods = set()
    def can_fit(self, pod):
        return self.alive and self.used_cpu + pod.cpu <= self.cpu and self.used_mem + pod.mem <= self.mem
    def place(self, pod):
        self.used_cpu += pod.cpu; self.used_mem += pod.mem; self.pods.add(pod)
    def remove(self, pod):
        self.used_cpu -= pod.cpu; self.used_mem -= pod.mem; self.pods.discard(pod)

class Pod:
    _ids = itertools.count()
    def __init__(self, cpu, mem):
        self.id = f"pod-{next(self._ids)}"; self.cpu = cpu; self.mem = mem
        self.status = "Pending"; self.node = None
