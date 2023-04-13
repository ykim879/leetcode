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
        :rtype: TreeNode
        """
        def buildTree(sp, ep, si, ei):
            if sp >= ep:
                return None
            if sp == ep - 1:
                return TreeNode(preorder[sp])
            i = 0
            while preorder[sp] != inorder[si + i]:
                i += 1
            if i == 0:
                left_child = None
            else:
                left_child = buildTree(sp + 1, sp + i + 1, si, si + i)
            right_child = buildTree(sp + i + 1, ep, si + i + 1, ei)
            return TreeNode(preorder[sp], left_child, right_child)
        return buildTree(0, len(preorder), 0, len(inorder))
