# 29. Maze Solver & Generator
import random
from collections import deque

def generate(w, h):
    grid = [[0]*w for _ in range(h)]
    def carve(x, y):
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        random.shuffle(dirs)
        for dx, dy in dirs:
            nx, ny = x+dx*2, y+dy*2
            if 0 <= nx < w and 0 <= ny < h and grid[ny][nx] == 0:
                grid[y+dy][x+dx] = 1
                grid[ny][nx] = 1
                carve(nx, ny)
    grid[1][1] = 1
    carve(1,1)
    return grid

def solve(grid, start, end):
    h, w = len(grid), len(grid[0])
    q = deque([start]); prev = {start: None}
    while q:
        x,y = q.popleft()
        if (x,y)==end: break
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<w and 0<=ny<h and grid[ny][nx]==1 and (nx,ny) not in prev:
                prev[(nx,ny)] = (x,y); q.append((nx,ny))
    path = []
    cur = end
    while cur and cur in prev:
        path.append(cur); cur = prev[cur]
    return list(reversed(path))

if __name__ == "__main__":
    g = generate(21, 21)
    path = solve(g, (1,1), (19,19))
    print("Path length:", len(path))
