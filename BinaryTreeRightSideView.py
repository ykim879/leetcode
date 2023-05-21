# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Beats 100% storage 
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # at each level pick right most val
        res = []
        curLevel = [root]
        while len(curLevel) > 0 and curLevel[0]:
            res.append(curLevel[-1].val)
            nextLevel = []
            for cur in curLevel:
                if cur.left:
                    nextLevel.append(cur.left)
                if cur.right:
                    nextLevel.append(cur.right)
            curLevel = nextLevel
        return res
