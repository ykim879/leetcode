# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def sumNumbersRecur(cur):
            if not cur.left and not cur.right:
                return [(cur.val, 0)]
            res = []
            if cur.left:
                for v, d in sumNumbersRecur(cur.left):
                    d += 1
                    res.append((v + cur.val *( 10 ** d), d))
            if cur.right:
                for v, d in sumNumbersRecur(cur.right):
                    d += 1
                    res.append((v + cur.val * (10 ** d), d))
            return res
        res = 0
        for v, _ in sumNumbersRecur(root):
            res += v
        return res
