# server.py
import asyncio
from .player import Player
from .room import Room
from .matchmaking import Matchmaker

TICK_HZ = 20

class GameServer:
    def __init__(self):
        self.rooms = {}
        self.players = {}
        self.mm = Matchmaker()

    def connect_player(self, pid):
        self.players[pid] = Player(pid)
        self.mm.join(pid)

    async def matchmaking_loop(self):
        while True:
            rid, ids = self.mm.pop_ready()
            if rid:
                room = Room(rid)
                for pid in ids:
                    room.add(self.players[pid])
                self.rooms[rid] = room
                print(f"Room {rid} created with {ids}")
            await asyncio.sleep(0.1)

    async def game_loop(self):
        dt = 1.0 / TICK_HZ
        while True:
            for room in self.rooms.values():
                room.step()
            await asyncio.sleep(dt)
