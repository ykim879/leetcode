# Beats 92%
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        #leftMost is smallest - getting to leftMost is O(logN) after traverse back for kth steps
        def kthSmallest(cur, kth):
            res = None
            if cur.left:
                res, kth = kthSmallest(cur.left, kth)
            kth += 1
            if res == None:
                if kth == k:
                    return cur.val, kth
                if cur.right:
                    res, kth = kthSmallest(cur.right, kth)
            return res, kth
        return kthSmallest(root, 0)[0]
