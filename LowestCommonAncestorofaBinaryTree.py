# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def lowestCommonAncestor(cur):
            if not cur:
                return None, False, False
            res, pFound, qFound = lowestCommonAncestor(cur.left)
            if not res:
                res, prFound, qrFound = lowestCommonAncestor(cur.right)
                pFound, qFound = max(pFound, prFound), max(qFound, qrFound)
            if not res:
                if cur.val == p.val:
                    pFound = True
                if cur.val == q.val:
                    qFound = True
                if pFound and qFound:
                    return cur, pFound, qFound
            return res, pFound, qFound
        return lowestCommonAncestor(root)[0]
        
