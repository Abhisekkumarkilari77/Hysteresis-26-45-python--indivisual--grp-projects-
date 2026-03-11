# 34. Spell Checker
import string

def edits1(word):
    letters = string.ascii_lowercase
    splits = [(word[:i], word[i:]) for i in range(len(word)+1)]
    deletes = [L + R[1:] for L,R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L,R in splits if len(R)>1]
    replaces = [L + c + R[1:] for L,R in splits if R for c in letters]
    inserts = [L + c + R for L,R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

class SpellChecker:
    def __init__(self, words):
        self.dict = set(w.lower() for w in words)

    def suggest(self, word):
        word = word.lower()
        if word in self.dict:
            return word
        candidates = [w for w in edits1(word) if w in self.dict]
        return min(candidates, key=len) if candidates else None

if __name__ == "__main__":
    sc = SpellChecker(["python","pytorch","pycharm"])
    print(sc.suggest("pythn"))
