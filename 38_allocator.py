# 38. Custom Memory Allocator
class Block:
    def __init__(self, start, size, free=True):
        self.start, self.size, self.free = start, size, free

class Allocator:
    def __init__(self, size):
        self.blocks = [Block(0, size, True)]

    def malloc(self, size):
        for b in self.blocks:
            if b.free and b.size >= size:
                if b.size > size:
                    self.blocks.insert(self.blocks.index(b)+1, Block(b.start+size, b.size-size, True))
                b.size = size; b.free = False
                return b.start
        return None

    def free(self, ptr):
        for b in self.blocks:
            if b.start == ptr:
                b.free = True; self._merge(); return True
        return False

    def _merge(self):
        merged=[]
        for b in self.blocks:
            if merged and merged[-1].free and b.free:
                merged[-1].size += b.size
            else:
                merged.append(b)
        self.blocks = merged

if __name__ == "__main__":
    a = Allocator(100)
    p1 = a.malloc(20); p2 = a.malloc(30)
    a.free(p1); a.free(p2)
    print([(b.start, b.size, b.free) for b in a.blocks])
