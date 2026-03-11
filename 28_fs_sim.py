# 28. File System Simulator
class Node:
    def __init__(self, name, is_dir):
        self.name = name
        self.is_dir = is_dir
        self.children = {} if is_dir else None
        self.content = "" if not is_dir else None

class FileSystem:
    def __init__(self):
        self.root = Node("/", True)
        self.cwd = self.root

    def _resolve(self, path):
        node = self.root if path.startswith("/") else self.cwd
        parts = [p for p in path.split("/") if p]
        for p in parts:
            if not node.is_dir or p not in node.children:
                return None
            node = node.children[p]
        return node

    def mkdir(self, path):
        parent_path, name = path.rsplit("/", 1) if "/" in path else ("", path)
        parent = self._resolve(parent_path) if parent_path else self.cwd
        if parent and parent.is_dir and name not in parent.children:
            parent.children[name] = Node(name, True)

    def touch(self, path, content=""):
        parent_path, name = path.rsplit("/", 1) if "/" in path else ("", path)
        parent = self._resolve(parent_path) if parent_path else self.cwd
        if parent and parent.is_dir:
            parent.children[name] = Node(name, False)
            parent.children[name].content = content

    def ls(self, path="."):
        node = self._resolve(path) if path != "." else self.cwd
        return sorted(node.children.keys()) if node and node.is_dir else []

    def cd(self, path):
        node = self._resolve(path)
        if node and node.is_dir:
            self.cwd = node

    def cat(self, path):
        node = self._resolve(path)
        return node.content if node and not node.is_dir else ""

    def rm(self, path):
        parent_path, name = path.rsplit("/", 1) if "/" in path else ("", path)
        parent = self._resolve(parent_path) if parent_path else self.cwd
        if parent and name in parent.children:
            del parent.children[name]

if __name__ == "__main__":
    fs = FileSystem()
    fs.mkdir("docs")
    fs.touch("docs/file.txt", "hello")
    print(fs.ls("docs"))
    print(fs.cat("docs/file.txt"))
