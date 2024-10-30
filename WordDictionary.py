class TrieNode:
    def __init__(self):
        self.children = {} # key: character value: node
        self.endofword = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endofword = True
    def search(self, word: str) -> bool:
        def dfs(cur, i): 
            ## check end of word
            if i == len(word):
                return cur.endofword
            # when we get ".": each character in cur.children with the rest of the word (i+1)
            if word[i] == ".":
                for nxt in cur.children.values():
                    if dfs(nxt, i+1):
                        return True
                return False
            # else we are going to see word[i] in cur, if it doesn't we are going to return false 
            if word[i] not in cur.children:
                return False
            # if it does we want to do dfs by incremening and updating current
            return dfs(cur.children[word[i]], i + 1)
        return dfs(self.root, 0)
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
