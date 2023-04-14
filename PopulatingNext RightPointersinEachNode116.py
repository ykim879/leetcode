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
        if not root or not root.left:
            return root
        d = deque([None])
        current = root
        while d:
            if not current:
                d.append(None)
                current = d.popleft()
                continue
            current.next = d.popleft()
            if current and current.left:
                d.append(current.left)
                d.append(current.right)
            current = current.next
        return root
