class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lowestCommonAncestor(cur):
            if not cur:
                return False, False, None
            pFound = qFound = False
            if cur == p:
                pFound = True
            if cur == q:
                qFound = True
            if cur.val > p.val or cur.val > q.val:
                pFoundL, qFoundL, anc = lowestCommonAncestor(cur.left)
                if anc:
                    return True, True, anc
                pFound = pFound | pFoundL
                qFound = qFound | qFoundL
            if cur.val < p.val or cur.val < q.val:
                pFoundR, qFoundR, anc = lowestCommonAncestor(cur.right)
                if anc:
                    return True, True, anc
                pFound = pFound | pFoundR
                qFound = qFound | qFoundR
            if pFound and qFound:
                return True, True, cur
            return pFound, qFound, None
        return lowestCommonAncestor(root)[2]
