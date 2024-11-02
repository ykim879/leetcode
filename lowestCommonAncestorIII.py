"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # parents want to know if pfound, qfound, res: if not res and pfound and qfound: res = cur
        parents = set([p])
        while p.parent:
            p = p.parent
            if p == q:
                return q
            parents.add(p)
        while q.parent:
            q = q.parent
            if q in parents:
                return q
