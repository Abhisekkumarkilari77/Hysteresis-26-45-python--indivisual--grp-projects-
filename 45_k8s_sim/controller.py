# controller.py
import random
from .models import Node, Pod
from .scheduler import Scheduler

class Controller:
    def __init__(self):
        self.scheduler = Scheduler()
    def bootstrap(self):
        for i, cpu in enumerate([4, 8, 16]):
            self.scheduler.add_node(Node(f"node-{i}", cpu, cpu*1024))
    def submit_workload(self, count=10):
        for _ in range(count):
            cpu = random.choice([1, 2, 4]); mem = cpu*256
            self.scheduler.submit(Pod(cpu, mem))
    def tick(self, steps=20):
        for _ in range(steps):
            self.scheduler.schedule()
    def fail_first_node(self):
        node = self.scheduler.nodes[0]; node.alive = False
        for pod in list(node.pods):
            node.remove(pod); pod.status = "Pending"; pod.node = None; self.scheduler.submit(pod)
    def report(self):
        for n in self.scheduler.nodes:
            print(n.name, "alive" if n.alive else "dead", "pods", [p.id for p in n.pods])
