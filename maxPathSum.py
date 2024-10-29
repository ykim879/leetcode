# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxPathSumRec(cur):
            if not cur:
                return -1001, 0
            maxPathL, maxPathLC = maxPathSumRec(cur.left)
            maxPathR, maxPathRC = maxPathSumRec(cur.right)
            includingCurrent = max(maxPathLC, maxPathRC, 0) + cur.val
            return max(maxPathL, maxPathR, includingCurrent, maxPathLC + maxPathRC + cur.val), includingCurrent
        return maxPathSumRec(root)[0]
