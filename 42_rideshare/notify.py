# notify.py
from typing import Callable

def stdout_notifier(event: str, data: dict):
    print(f"[{event}] {data}")

class Notifier:
    def __init__(self, sink: Callable[[str, dict], None] = stdout_notifier):
        self.sink = sink
    def emit(self, event: str, data: dict):
        self.sink(event, data)
