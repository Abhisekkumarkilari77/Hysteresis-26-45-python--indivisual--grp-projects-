#!/usr/bin/env python
# main.py
from .crawler import Crawler

def fake_fetch(url: str) -> str:
    # stub fetcher; replace with httpx + robots.txt
    return f"<html><head><title>{url}</title></head><body><a href='{url}/child'>child</a>{url} body</body></html>"

def run():
    c = Crawler(fake_fetch)
    c.crawl(["http://example.com"], limit=10)
    print("Search 'example':", c.search("example"))

if __name__ == "__main__":
    run()
