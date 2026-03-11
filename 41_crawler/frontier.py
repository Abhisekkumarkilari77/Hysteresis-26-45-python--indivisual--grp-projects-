# frontier.py
import heapq
from dataclasses import dataclass, field
from typing import Set, Tuple

@dataclass(order=True)
class FrontierItem:
    priority: float
    url: str = field(compare=False)

class Frontier:
    def __init__(self):
        self.heap: list[FrontierItem] = []
        self.seen: Set[str] = set()
    def add(self, url: str, priority: float = 0.0):
        if url in self.seen:
            return
        heapq.heappush(self.heap, FrontierItem(priority, url))
        self.seen.add(url)
    def pop(self) -> str | None:
        return heapq.heappop(self.heap).url if self.heap else None
    def __len__(self):
        return len(self.heap)
