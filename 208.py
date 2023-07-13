class Trie(object):

    def __init__(self):
        self.endOfWord = False
        self.children = [None for _ in range(26)]

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self
        for w in word:
            i = ord(w) - ord("a")
            if not cur.children[i]:
                cur.children[i] = Trie()
            cur = cur.children[i]
        cur.endOfWord = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cur = self
        for w in word:
            if not cur:
                break
            i = ord(w) - ord("a")
            cur = cur.children[i]
        return cur and cur.endOfWord

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        cur = self
        for w in prefix:
            if not cur:
                break
            i = ord(w) - ord("a")
            cur = cur.children[i]
        return cur != None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
