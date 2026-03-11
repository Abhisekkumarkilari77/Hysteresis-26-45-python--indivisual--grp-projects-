# 31. Social Network Friend Graph
from collections import defaultdict, deque

class SocialGraph:
    def __init__(self):
        self.g = defaultdict(set)

    def add_user(self, u):
        self.g[u]

    def add_friend(self, a, b):
        self.g[a].add(b); self.g[b].add(a)

    def remove_friend(self, a, b):
        self.g[a].discard(b); self.g[b].discard(a)

    def mutual(self, a, b):
        return self.g[a] & self.g[b]

    def recommend(self, user):
        candidates = defaultdict(int)
        for friend in self.g[user]:
            for fof in self.g[friend]:
                if fof != user and fof not in self.g[user]:
                    candidates[fof] += 1
        return sorted(candidates, key=candidates.get, reverse=True)

    def shortest_path(self, start, goal):
        q = deque([start]); prev = {start: None}
        while q:
            u = q.popleft()
            if u == goal: break
            for v in self.g[u]:
                if v not in prev:
                    prev[v] = u; q.append(v)
        path = []
        cur = goal
        while cur in prev and cur is not None:
            path.append(cur); cur = prev[cur]
        return list(reversed(path))

if __name__ == "__main__":
    sg = SocialGraph()
    sg.add_friend("Alice","Bob"); sg.add_friend("Bob","Charlie")
    print("Recommend for Alice:", sg.recommend("Alice"))
    print("Path Alice->Charlie:", sg.shortest_path("Alice","Charlie"))
