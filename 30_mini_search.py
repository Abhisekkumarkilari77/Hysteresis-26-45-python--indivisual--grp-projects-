# 30. Mini Search Engine
import math
import re
from collections import defaultdict, Counter

TOKEN = re.compile(r"\b[a-zA-Z]+\b")

class MiniSearch:
    def __init__(self):
        self.docs = {}
        self.inv = defaultdict(dict)

    def add_doc(self, doc_id, text):
        self.docs[doc_id] = text
        tokens = [t.lower() for t in TOKEN.findall(text)]
        counts = Counter(tokens)
        for term, freq in counts.items():
            self.inv[term][doc_id] = freq

    def search(self, query, top_k=5):
        terms = [t.lower() for t in TOKEN.findall(query)]
        scores = defaultdict(float)
        N = len(self.docs) or 1
        for term in terms:
            postings = self.inv.get(term, {})
            idf = math.log(N / (1 + len(postings)))
            for doc, tf in postings.items():
                scores[doc] += tf * idf
        return sorted(scores.items(), key=lambda x: -x[1])[:top_k]

if __name__ == "__main__":
    ms = MiniSearch()
    ms.add_doc(1, "Python tutorial with basics")
    ms.add_doc(2, "Advanced tutorial for python and data")
    print(ms.search("python tutorial"))
