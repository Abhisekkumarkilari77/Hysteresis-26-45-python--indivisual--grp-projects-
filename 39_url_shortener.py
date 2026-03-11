# 39. URL Shortener Backend
import string, random
BASE62 = string.ascii_letters + string.digits

class URLShortener:
    def __init__(self):
        self.map = {}; self.rev = {}

    def _gen_id(self, length=6):
        while True:
            sid = "".join(random.choice(BASE62) for _ in range(length))
            if sid not in self.map:
                return sid

    def shorten(self, long_url):
        if long_url in self.rev: return self.rev[long_url]
        sid = self._gen_id(); self.map[sid] = long_url; self.rev[long_url] = sid
        return sid

    def resolve(self, sid):
        return self.map.get(sid)

if __name__ == "__main__":
    s = URLShortener()
    sid = s.shorten("https://example.com")
    print(sid, "->", s.resolve(sid))
