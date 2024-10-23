# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def recur(cur):
            if not cur:
                return None, None
            lefthead, lefttail = recur(cur.left)
            righthead, righttail = recur(cur.right)
            if lefthead:
                cur.right = lefthead
            if lefttail:
                lefttail.right = righthead
            else:
                cur.right = righthead
            cur.left = None
            if not righttail:
                if not lefttail:
                    return cur, cur
                else:
                    return cur, lefttail
            return cur, righttail
        recur(root)
