# pagerank.py
from typing import Dict, Iterable


def pagerank(graph: Dict[str, Iterable[str]], damping: float = 0.85, iters: int = 10) -> Dict[str, float]:
    nodes = list(graph.keys()) or ["dummy"]
    N = len(nodes)
    rank = {n: 1 / N for n in nodes}
    out = {n: len(graph[n]) for n in nodes}
    for _ in range(iters):
        nr = {n: (1 - damping) / N for n in nodes}
        for n in nodes:
            if out[n] == 0:
                continue
            share = damping * rank[n] / out[n]
            for dst in graph[n]:
                if dst in nr:
                    nr[dst] += share
        rank = nr
    return rank
