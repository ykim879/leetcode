class Trie(object):
    def __init__(self):
        self.eow = False
        self.children = {}
class WordDictionary(object):

    def __init__(self):
        self.root = Trie()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root
        for w in word:
            if not cur.children.get(w):
                cur.children[w] = Trie()
            cur = cur.children[w]
        cur.eow = True
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def search(cur, word):
            if word == '.':
                for n in cur.children.values():
                    if n.eow:
                        return True
                return False
            for i, w in enumerate(word):
                if w == '.':
                    for n in cur.children.values():
                        if search(n, word[i+1:]):
                            return True
                    return False
                else:
                    if cur.children.get(w):
                        cur = cur.children[w]
                    else:
                        return False
            return cur.eow
        return search(self.root, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
