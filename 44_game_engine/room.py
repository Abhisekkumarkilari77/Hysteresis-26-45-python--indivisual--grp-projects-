# room.py
class Room:
    def __init__(self, room_id):
        self.id = room_id
        self.players = {}
    def add(self, player):
        self.players[player.id] = player
    def step(self):
        for p in self.players.values():
            p.hp = min(100, p.hp + 0.1)
