# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        def recur(cur):
            if not cur or (not cur.left and not cur.right):
                return cur, cur
            leftHead, leftEnd = recur(cur.left)
            if leftEnd:
                leftEnd.right = cur
            if not leftHead:
                leftHead = cur
            rightHead, rightEnd = recur(cur.right)
            cur.right = rightHead
            if not rightEnd:
                rightEnd = cur
                cur.right = None
            return leftHead, rightEnd
        self.current, _ = recur(root)
        self.current = TreeNode(0, None, self.current)

        

    def next(self):
        """
        :rtype: int
        """
        self.current = self.current.right
        return self.current.val

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.current.right != None


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
