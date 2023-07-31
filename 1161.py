class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        from collections import Counter
        levels = Counter()
        def maxLevelSum(cur, level):
            if not cur:
                return
            levels[level] += cur.val
            maxLevelSum(cur.right, level + 1)
            maxLevelSum(cur.left, level + 1)
        maxLevelSum(root, 1)
        return max(levels, key=levels.get)
