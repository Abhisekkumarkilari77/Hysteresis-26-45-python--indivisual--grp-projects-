# 27. Autocomplete System
from collections import defaultdict
TOP_K = 5

class TrieNode:
    def __init__(self):
        self.children = {}
        self.freq = 0
        self.end = False

class AutoComplete:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, freq=1):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.end = True
        node.freq += freq

    def _dfs(self, node, prefix, out):
        if node.end:
            out.append((node.freq, prefix))
        for ch, nxt in node.children.items():
            self._dfs(nxt, prefix + ch, out)

    def suggest(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        results = []
        self._dfs(node, prefix, results)
        results.sort(key=lambda x: (-x[0], x[1]))
        return [w for _, w in results[:TOP_K]]

if __name__ == "__main__":
    ac = AutoComplete()
    for w, f in [("python", 10), ("pytorch", 7), ("pycharm", 5), ("pyramid", 2), ("py", 1)]:
        ac.insert(w, f)
    print(ac.suggest("py"))
