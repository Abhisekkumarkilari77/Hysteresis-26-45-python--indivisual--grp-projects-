#!/usr/bin/env python
# main.py
import asyncio
from .server import GameServer

def run_demo():
    gs = GameServer()
    for pid in ["p1","p2","p3","p4"]:
        gs.connect_player(pid)
    return gs

async def main():
    gs = run_demo()
    await asyncio.gather(gs.matchmaking_loop(), gs.game_loop())

if __name__ == "__main__":
    asyncio.run(main())
