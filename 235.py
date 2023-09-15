# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # get current return False False None if it is null
        # do left check if parent if not do right and check if parent if not do current and if both are two return curr otherwise none
        def lowestCommonAncestor(cur):
            if not cur:
                return False, False, None
            pFound, qFound, anc = lowestCommonAncestor(cur.left)
            if anc:
                return True, True, anc
            pFoundR, qFoundR, anc = lowestCommonAncestor(cur.right)
            if anc:
                return True, True, anc
            pFound = pFound | pFoundR
            qFound = qFound | qFoundR
            if cur == p:
                pFound = True
            elif cur == q:
                qFound = True
            if pFound and qFound:
                return True, True, cur
            return pFound, qFound, None
        return lowestCommonAncestor(root)[2]

            
        
