# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generateTrees(n, start):
            if n == 1:
                v = TreeNode(start)
                return [v]
            res = []
            total = n-1
            end = total % 2
            for n_ in range(total // 2 + end):
                if n_ == 0:
                    children = generateTrees(total, start)
                    for child in children:
                        root = TreeNode(start + total)
                        root.left = child
                        res.append(root)
                    children = generateTrees(total, start + 1)
                    for child in children:
                        root = TreeNode(start)
                        root.right = child
                        res.append(root)
                else:
                    children1 = generateTrees(n_, start)
                    children2 = generateTrees(total - n_, n_ + start + 1)
                    for child1 in children1:
                        for child2 in children2:
                            root = TreeNode(start + n_)
                            root.left = child1
                            root.right = child2
                            res.append(root)
                    children1 = generateTrees(n_, total - n_ + start + 1)
                    children2 = generateTrees(total - n_, start)
                    for child1 in children1:
                        for child2 in children2:
                            root = TreeNode(total - n_ + start)
                            root.left = child2
                            root.right = child1
                            res.append(root)
            if end == 0:
                n_ = total // 2
                children1 = generateTrees(n_, start)
                children2 = generateTrees(total - n_, n_ + start + 1)
                for child1 in children1:
                    for child2 in children2:
                        root = TreeNode(start + n_)
                        root.left = child1
                        root.right = child2
                        res.append(root)
            return res
        return generateTrees(n, 1)
