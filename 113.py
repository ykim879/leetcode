# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # convety the children from top to bottom iterate until all queue is empty
        # recursion with path 
        from copy import copy
        path = []
        res = []
        def pathSumRecur(cur, targetSum, pathSum):
            path.append(cur.val)
            pathSum += cur.val 
            if not cur.left and not cur.right and targetSum == pathSum:
                newPath = copy(path)
                res.append(newPath)
            if cur.left:
                pathSumRecur(cur.left, targetSum, pathSum)
            if cur.right:
                pathSumRecur(cur.right, targetSum, pathSum)
            path.pop()
        if root:
            pathSumRecur(root, targetSum, 0)
        return res

