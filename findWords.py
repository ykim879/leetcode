class TrieNode:
    def __init__(self):
        self.children = {} # value is TrieNode
        self.endOfWord = None
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        R, C = len(board), len(board[0])
        res = set()
        root = TrieNode()
        visited = set()
        # build trie for words
        for word in words:
            cur = root
            for w in word:
                if w not in cur.children:
                    cur.children[w] = TrieNode()
                cur = cur.children[w]
            cur.endOfWord = word
        def dfs(r, c, node): # node is trie node (trie.childre)
            # base case: if r, c is out of range or r,c is in path or board[r][c] is not in trie.children
            if r < 0 or c < 0 or r >= R or c >= C or (r,c) in visited or board[r][c] not in node.children:
                return
            visited.add((r,c))
            cur = node.children[board[r][c]]
            # if trie is end of word add path to res
            if cur.endOfWord:
                res.add(cur.endOfWord)
            # dfs adjency 
            dfs(r+1, c, cur)
            dfs(r-1, c, cur)
            dfs(r, c+1, cur)
            dfs(r, c-1, cur)
            visited.remove((r,c))
            #node.visited.add((r,c))
        for r in range(R):
            for c in range(C): 
                dfs(r, c, root)
        return list(res)
