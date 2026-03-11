# parser.py
import re
from html.parser import HTMLParser
from typing import List

class SimpleHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links: List[str] = []
        self.title: str = ""
        self.text_parts: List[str] = []
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            href = dict(attrs).get("href")
            if href and href.startswith("http"):
                self.links.append(href)
        if tag == "title":
            self._in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        self.text_parts.append(data)

    @property
    def text(self) -> str:
        return " ".join(self.text_parts)

TOKEN_RE = re.compile(r"[a-zA-Z0-9]+")

def tokenize(text: str):
    return [t.lower() for t in TOKEN_RE.findall(text)]
