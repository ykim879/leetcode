# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # (1) root is always end of post order
        # (2) from left of the root in inorder is always leftNode and it is same for postorder. Knowing the size by inorder we can extract from post order
        # (3) from right of the root in order is always rightNode
        def buildTree(iS, iE, pS, pE):
            root, rootNode = postorder[pE], TreeNode(postorder[pE])
            # build leftNode
            lE = iS
            while inorder[lE] != root:
                lE += 1
            if lE == iS + 1: #there is only one Node (not a tree) - better to do it before recursive to save time
                rootNode.left = TreeNode(inorder[iS])
            elif lE > iS:
                rootNode.left = buildTree(iS, lE - 1, pS, pS + (lE - iS -1))
            if lE == iE - 1:
                rootNode.right = TreeNode(inorder[iE])
            elif lE < iE:
                rootNode.right = buildTree(lE + 1, iE,pS + (lE - iS), pE - 1)
            return rootNode
        return buildTree(0, len(inorder) - 1, 0, len(postorder) - 1)
            
                
