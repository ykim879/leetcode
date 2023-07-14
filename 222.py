# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        #go down to the right child and do the level
        cur, level = root, 0
        while cur:
            if not cur.right:
                break
            cur = cur.right
            level += 1
        # level first search bfs - go to level and if the level check the children is empty
        children = 0
        for l in range(level + 2):
            children += 2 ** l

        s = [(root, 0)]
        
        while s:
            cur, l = s.pop()
            if l == level:
                if cur.right:
                    break
                children -= 1
                if cur.left:
                    break
                children -= 1
            else:
                l += 1
                s.append((cur.left, l))
                s.append((cur.right, l))
        return children
