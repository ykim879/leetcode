# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        queue = deque([(root, 0)])
        res = deque([])
        while queue:
            cur, level = queue.popleft()
            if cur:
                if not res or len(res) <= level:
                    res.appendleft(list())
                res[0].append(cur.val)
                level += 1
                queue.append((cur.left, level))
                queue.append((cur.right, level))
        return res
        
