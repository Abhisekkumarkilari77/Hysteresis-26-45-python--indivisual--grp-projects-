# crawler.py
import hashlib
from collections import defaultdict
from .frontier import Frontier
from .parser import SimpleHTMLParser, tokenize
from .indexer import InvertedIndex
from .pagerank import pagerank

class Crawler:
    def __init__(self, fetch_html):
        self.frontier = Frontier()
        self.fetch_html = fetch_html
        self.graph = defaultdict(set)
        self.index = InvertedIndex()
        self.hashes = set()
        self.page_rank = {}

    def crawl(self, seeds, limit=50):
        for s in seeds:
            self.frontier.add(s, 0)
        while len(self.frontier) and limit > 0:
            url = self.frontier.pop(); limit -= 1
            self._process(url)
        self.page_rank = pagerank(self.graph)

    def _process(self, url):
        html = self.fetch_html(url)
        if html is None:
            return
        digest = hashlib.sha256(html.encode()).hexdigest()
        if digest in self.hashes:
            return
        self.hashes.add(digest)
        parser = SimpleHTMLParser(); parser.feed(html)
        tokens = tokenize(parser.text)
        self.index.add_doc(url, tokens, parser.text)
        for link in parser.links:
            self.graph[url].add(link)
            self.frontier.add(link, priority=1)

    def search(self, query):
        return self.index.search(query, self.page_rank)
