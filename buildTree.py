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
        # Create a hashmap to store indices of inorder elements
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
        
        def recur(pi, pj, ii, ij):
            # base case: index out of bound
            if pi >= pj or ii >= ij:
                return None
            
            # Get the root value from preorder
            cur = preorder[pi]
            # Find the root index in the inorder list using the hashmap
            ri = inorder_index_map[cur]
            
            # Calculate the length of the left subtree
            leftlength = ri - ii
            
            # Recursively construct the left and right subtrees
            leftNode = recur(pi + 1, pi + 1 + leftlength, ii, ri)
            rightNode = recur(pi + 1 + leftlength, pj, ri + 1, ij)
            
            # Return the root node
            return TreeNode(cur, leftNode, rightNode)
        
        return recur(0, len(preorder), 0, len(inorder))
