"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
"""
explaination: divide grid into four and if they are all leaf and have same value merge them otherwise, return separately
"""
class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        def construct(x1, x2, y1, y2):
            if x2 - x1 == 0:
                return None, None
            elif x2 - x1 == 1:
                return Node(grid[y1][x1], 1)
            k = (x2-x1)//2
            topLeft = construct(x1, x1+k, y1, y1+k)
            topRight = construct(x1+k, x2, y1, y1+k)
            bottomLeft = construct(x1, x1+k, y1+k, y2)
            bottomRight = construct(x1+k, x2, y1+k, y2)
            if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and \
            topLeft.val == topRight.val and topLeft.val == bottomLeft.val and bottomLeft.val == bottomRight.val:
                return Node(topLeft.val, 1)
            return Node(0, 0, topLeft, topRight, bottomLeft, bottomRight)
        return construct(0, len(grid), 0, len(grid))
