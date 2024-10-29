# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # DSF : input: minimum, maximum, cur return: bool indicating if it is validBST
        def dsf(minimum, maximum, cur):
            ## base case (1) node null return True
            if not cur:
                return True
            ## base case (2) node is not in this range
            if not (minimum < cur.val < maximum):
                return False
            ## to right: minimum should be current node and maximum is same
            ## to left: maximum should be current value and minimum is same
            return dsf(cur.val, maximum, cur.right) and dsf(minimum, cur.val, cur.left)
        return dsf(-2**31-1, 2**31, root)
