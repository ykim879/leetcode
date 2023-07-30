# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def longestZigZag(cur, dirR, lth):
            if not cur:
                return lth
            if dirR:
                return max(longestZigZag(cur.left, False, lth + 1), longestZigZag(cur.right, True, 0))
            return max(longestZigZag(cur.right, True, lth + 1), longestZigZag(cur.left, False, 0))
        return max(longestZigZag(root.right, True, 0), longestZigZag(root.left, False, 0))
