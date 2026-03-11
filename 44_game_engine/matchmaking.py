# matchmaking.py
from collections import deque
ROOM_SIZE = 2

class Matchmaker:
    def __init__(self):
        self.queue = deque(); self.counter = 0
    def join(self, pid):
        self.queue.append(pid)
    def pop_ready(self):
        if len(self.queue) >= ROOM_SIZE:
            ids = [self.queue.popleft() for _ in range(ROOM_SIZE)]
            self.counter += 1
            return f"room-{self.counter}", ids
        return None, None
