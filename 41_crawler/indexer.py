# indexer.py
from collections import Counter, defaultdict
from typing import Dict, List, Tuple
from .parser import tokenize

class InvertedIndex:
    def __init__(self):
        self.index: Dict[str, List[Tuple[str, int]]] = defaultdict(list)
        self.docs: Dict[str, str] = {}

    def add_doc(self, doc_id: str, tokens: List[str], text: str):
        counts = Counter(tokens)
        for term, freq in counts.items():
            self.index[term].append((doc_id, freq))
        self.docs[doc_id] = text

    def search(self, query: str, pagerank: Dict[str, float], top_k: int = 5):
        terms = tokenize(query)
        scores = defaultdict(float)
        for term in terms:
            for doc, tf in self.index.get(term, []):
                scores[doc] += tf
        for doc in list(scores):
            scores[doc] += 0.5 * pagerank.get(doc, 0)
        return sorted(scores.items(), key=lambda x: -x[1])[:top_k]
