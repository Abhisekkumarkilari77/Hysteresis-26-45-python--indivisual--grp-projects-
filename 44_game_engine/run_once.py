import asyncio
import importlib.machinery, importlib.util, pathlib, sys
base = pathlib.Path(__file__).parent
spec = importlib.util.spec_from_file_location('game_main', base/'main.py')
mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)

gs = mod.run_demo()
async def main():
    t1 = asyncio.create_task(gs.matchmaking_loop())
    t2 = asyncio.create_task(gs.game_loop())
    await asyncio.sleep(1)
    t1.cancel(); t2.cancel()
    print('Rooms:', list(gs.rooms.keys()))

asyncio.run(main())
