# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def flattenRecur(cur):
            if not cur:
                return None
            if not cur.left and not cur.right:
                return cur
            tailL = flattenRecur(cur.left)
            tailR = flattenRecur(cur.right)
            if tailL:
                tailL.right = cur.right
                cur.right = cur.left
                cur.left = None
            if tailR:
                return tailR
            return tailL
        flattenRecur(root)
