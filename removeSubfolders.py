class TrieNode:
    def __init__(self):
        self.endofWord = False
        self.children = {} # key : character value: TrieNode
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = TrieNode()
        res = []
        folder.sort()
        for f in folder: # traverse the node and if the path's TrieNode.endofWord -> skip folder. otherwise we are going to add it
            current = root
            isSubfolder = False
            for c in f.split('/'):
                if c not in current.children:
                    current.children[c] = TrieNode()
                current = current.children[c]
                if current.endofWord:
                    isSubfolder = True
                    break
            if not isSubfolder:
                res.append(f)
                current.endofWord = True
        return res
