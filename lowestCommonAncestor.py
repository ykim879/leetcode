# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recur(cur):
            if not cur:
                return False, False, None
            p1, q1, res = recur(cur.left)
            if res:
                return p1, q1, res
            p2, q2, res = recur(cur.right)
            if res:
                return p2, q2, res
            found1 = p1 or p2 or p.val == cur.val
            found2 = q1 or q2 or q.val == cur.val
            if found1 and found2:
                res = cur
            return found1, found2, res
        return recur(root)[2]
