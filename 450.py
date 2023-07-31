# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def deleteNode(cur):
            if not cur.left and cur.right:
                return cur.right
            if cur.left and cur.right:
                n = cur.left
                while n.right:
                    n = n.right
                n.right = cur.right
            return cur.left
        def deleteNodeRecur(cur, key):
            if not cur: 
                return False, False
            if cur.val == key:
                return True, True
            found, parent = deleteNodeRecur(cur.left, key)
            if found:
                if parent:
                    cur.left = deleteNode(cur.left)
                return True, False
            found, parent = deleteNodeRecur(cur.right, key)
            if found:
                if parent:
                    cur.right = deleteNode(cur.right)
                return True, False
            return False, False
        _, parent = deleteNodeRecur(root, key)
        if parent:
            return deleteNode(root)
        return root
