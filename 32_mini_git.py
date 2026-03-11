# 32. Mini Git
import hashlib
import json
from datetime import datetime

class MiniGit:
    def __init__(self):
        self.index = {}
        self.commits = []

    def add(self, path, content):
        self.index[path] = content

    def commit(self, message):
        snapshot = dict(self.index)
        commit_id = hashlib.sha1(json.dumps(snapshot, sort_keys=True).encode()).hexdigest()[:7]
        self.commits.append({
            "id": commit_id,
            "message": message,
            "timestamp": datetime.utcnow().isoformat(),
            "snapshot": snapshot,
        })
        return commit_id

    def log(self):
        return list(reversed(self.commits))

    def checkout(self, commit_id):
        for c in self.commits:
            if c["id"] == commit_id:
                self.index = dict(c["snapshot"])
                return True
        return False

if __name__ == "__main__":
    git = MiniGit()
    git.add("README.md", "hello")
    cid = git.commit("init")
    print(git.log())
    git.add("app.py", "print('hi')")
    git.commit("add app")
    git.checkout(cid)
    print("Index after checkout:", git.index)
