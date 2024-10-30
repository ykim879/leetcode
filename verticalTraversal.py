# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hq = []
        # vertical ordering: (c, r, cur.val) asc value - bfs/ dfs -> save memory by using dfs 
        def dfs(r, c, cur):
            if not cur:
                return
            heapq.heappush(hq, (c, r, cur.val))
            dfs(r+1, c-1, cur.left)
            dfs(r+1, c+1, cur.right)
        dfs(0, 0, root)
        # top
        res = []
        offset = hq[0][0]
        while hq:
            c, r, val = heapq.heappop(hq)
            c -= offset
            if c >= len(res):
                res.append([])
            res[c].append(val)
        return res
