# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def recur(cur, cursum, path):
            if not cur:
                return 0
            path += str(cur.val)
            if not cur.left and not cur.right: # sum all string value of path into integer and add to cursum
                cursum += int(path)
                return cursum
            return recur(cur.left, cursum, path) + recur(cur.right, cursum, path)
        return recur(root, 0, "")     
