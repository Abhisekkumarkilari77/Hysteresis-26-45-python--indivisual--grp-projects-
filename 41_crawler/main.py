#!/usr/bin/env python
# main.py
"""
Tiny "mini-Google" CLI:
- crawls a few seed URLs (stubbed fetcher)
- then lets you type queries and shows ranked results.
"""
import sys

from .crawler import Crawler


def fake_fetch(url: str) -> str:
    # stub fetcher; replace with httpx + robots.txt
    return (
        f"<html><head><title>{url}</title></head>"
        f"<body><a href='{url}/child'>child</a>{url} body</body></html>"
    )


def run():
    crawler = Crawler(fake_fetch)
    # Seed with a few hosts; replace with live URLs when using a real fetcher.
    seeds = ["http://example.com", "http://example.org", "http://google.com"]
    crawler.crawl(seeds, limit=20)

    # If a query is given as CLI arg, search once and exit.
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        print("Search results:", crawler.search(query))
        return

    # Simple REPL for searching.
    print("Mini search ready. Type a query (or 'exit').")
    while True:
        try:
            q = input("> ").strip()
        except EOFError:
            break
        if not q or q.lower() in {"exit", "quit"}:
            break
        results = crawler.search(q)
        if not results:
            print("No results.")
        else:
            for rank, (doc, score) in enumerate(results, 1):
                print(f"{rank}. {doc} (score={score:.3f})")


if __name__ == "__main__":
    run()
