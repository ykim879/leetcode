"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        # each level, set next to each other
        # queue (node, level) pop next and if popnext is as same level as current level then do next.right
        q = deque([(root, 0)])
        while q:
            cur, level = q.popleft()
            if q and q[0][1] == level:
                cur.next = q[0][0]
            level += 1
            if cur.left:
                q.append((cur.left, level))
            if cur.right:
                q.append((cur.right, level))
        return root
