# scheduler.py
from collections import deque
from typing import List
from .models import Node, Pod

class Scheduler:
    def __init__(self, policy="least_loaded"):
        self.policy = policy
        self.nodes: List[Node] = []
        self.pending = deque()

    def add_node(self, node: Node):
        self.nodes.append(node)

    def submit(self, pod: Pod):
        self.pending.append(pod)

    def schedule(self):
        if not self.pending:
            return
        pod = self.pending[0]
        node = self._select_node(pod)
        if node:
            self.pending.popleft()
            node.place(pod); pod.node = node; pod.status = "Running"

    def _select_node(self, pod):
        candidates = [n for n in self.nodes if n.can_fit(pod)]
        if not candidates:
            return None
        if self.policy == "round_robin":
            chosen = candidates[0]; self.nodes = self.nodes[1:] + self.nodes[:1]; return chosen
        return min(candidates, key=lambda n: n.used_cpu)
