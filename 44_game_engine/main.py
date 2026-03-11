#!/usr/bin/env python
# main.py
import asyncio
import os
from .server import GameServer

def run_demo():
    gs = GameServer()
    for pid in ["p1", "p2", "p3", "p4"]:
        gs.connect_player(pid)
    return gs

async def main(duration: float | None = None):
    gs = run_demo()
    task1 = asyncio.create_task(gs.matchmaking_loop())
    task2 = asyncio.create_task(gs.game_loop())
    if duration is None:
        await asyncio.gather(task1, task2)
    else:
        await asyncio.sleep(duration)
        task1.cancel()
        task2.cancel()
        print("Rooms:", list(gs.rooms.keys()))

if __name__ == "__main__":
    dur = float(os.getenv("DEMO_DURATION", "0"))
    asyncio.run(main(dur if dur > 0 else None))
