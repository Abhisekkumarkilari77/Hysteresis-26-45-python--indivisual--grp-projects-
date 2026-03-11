# player.py
import math
MAX_SPEED = 5.0

class Player:
    def __init__(self, pid):
        self.id = pid; self.x = 0; self.y = 0; self.hp = 100
    def move(self, dx, dy):
        if math.hypot(dx, dy) > MAX_SPEED:
            return False
        self.x += dx; self.y += dy; return True
