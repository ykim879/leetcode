# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        """
        :rtype: TreeNode
        """
        def recur(pi, pj, ii, ij):
            # base case: index out of bound
            if pi >= pj or ii >= ij:
                return None
            ri = ii
            cur = preorder[pi]
            while cur != inorder[ri]: # no bound check since it always exists before it goes out of bound
                ri += 1
            leftlength = ri - ii
            leftNode = recur(pi + 1, pi + 1 + leftlength, ii, ri) # if there is no leftNode/rightNode pi == pj so it will breal
            rightNode = recur(pi + 1 + leftlength, pj, ri + 1, ij)
            return TreeNode(cur, leftNode, rightNode)
        return recur(0, len(preorder), 0, len(preorder))
        
