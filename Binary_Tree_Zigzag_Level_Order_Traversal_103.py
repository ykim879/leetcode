# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = deque([(0, root)])
        next_level = deque()
        res = []
        while q:
            i, current = q.popleft()
            if len(res) <= i:
                new = [current.val]
                res.append(new)
            else:
                res[i].append(current.val)
            i += 1
            if current.left and current.right:
                if i%2:
                    next_level.appendleft((i, current.left))
                    next_level.appendleft((i, current.right))
                else:
                    next_level.appendleft((i, current.right))
                    next_level.appendleft((i, current.left))
            elif not current.left and current.right:
                next_level.appendleft((i, current.right))
            elif not current.right and current.left:
                next_level.appendleft((i, current.left))
            if not q and next_level:
                q.extend(next_level)
                next_level = deque()
        return res
