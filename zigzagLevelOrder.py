# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # level: even/odd -> different approach
        # level search: stack by level by level 
        res = []
        if not root:
            return res
        stack = [root]
        level = 0
        while stack:
            layer = []
            nextstack = []
            while stack:
                cur = stack.pop()
                if not cur:
                    continue
                layer.append(cur.val)
                if level % 2: # next level is even: left to right -> opposite
                    nextstack.append(cur.right)
                    nextstack.append(cur.left)
                else: # opposite
                    nextstack.append(cur.left)
                    nextstack.append(cur.right)
            level += 1
            stack.extend(nextstack)
            if layer:
                res.append(layer)
        return res

        
