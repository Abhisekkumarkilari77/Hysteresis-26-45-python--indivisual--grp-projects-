# 33. Log Analyzer
import re
from collections import Counter

LOG_RE = re.compile(r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(\w+) (.*?)" (\d{3})')

def parse_line(line):
    m = LOG_RE.match(line)
    return m.groups() if m else None

def analyze(lines):
    ips = Counter(); codes = Counter()
    for line in lines:
        parsed = parse_line(line)
        if not parsed: continue
        ip, _, method, path, code = parsed
        ips[ip] += 1; codes[code] += 1
    return ips.most_common(5), codes.most_common()

if __name__ == "__main__":
    sample = ['127.0.0.1 - - [01] "GET /home" 200',
              '10.0.0.2 - - [01] "POST /login" 401',
              '127.0.0.1 - - [01] "GET /about" 404']
    print(analyze(sample))
