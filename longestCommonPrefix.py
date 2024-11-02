class TrieNode:
    def __init__(self, val = 0):
        self.child = {} # key : character, value: TrieNode
        self.count = 0
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # build trie node with count
        root = TrieNode()
        L = len(strs)
        for s in strs:
            cur = root
            for c in s:
                if c not in cur.child:
                    cur.child[c] = TrieNode()
                cur = cur.child[c]
                cur.count += 1
        # do bfs stack queue if it next count > 1, if not update this with maxlength
        q = deque([(root, "")])
        while q:
            cur, path = q.popleft()
            for ch, nxt in cur.child.items():
                if nxt.count == L:
                    q.append((nxt, path + ch))
            if not q:
                return path
