# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.storeleft(root)

    def storeleft(self, cur):
        p = cur
        while p:
            self.stack.append(p)
            p = p.left

    def next(self) -> int:
        cur = self.stack.pop()
        self.storeleft(cur.right)
        return cur.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
