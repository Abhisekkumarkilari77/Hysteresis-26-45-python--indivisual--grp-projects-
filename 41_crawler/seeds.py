# seeds.py
# Synthetic list of 1000 student-friendly seed URLs.
# Using predictable placeholders to avoid external fetches.
SEEDS = [f"http://campus{i}.edu" for i in range(1, 1001)]
# A few recognizable educational domains (still stub-fetched).
SEEDS += [
    "http://wikipedia.org",
    "http://khanacademy.org",
    "http://coursera.org",
    "http://edx.org",
    "http://mit.edu",
    "http://stanford.edu",
]
