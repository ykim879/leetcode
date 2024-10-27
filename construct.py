"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def constructNode(i1, i2, j1, j2):
            if i2 - i1 == 1:
                return Node(grid[i1][j1], True,  None, None, None, None)
            h = (i2- i1) // 2
            # construct 4 nodes
            topleft, topright = constructNode(i1, i1+h, j1, j2 + h), constructNode(i1, i1+h, j1 + h, j2)
            bottomleft, bottomright = constructNode(i1 + h, i2, j1, j2 + h), constructNode(i1 + h, i2, j1 + h, j2)
            # if all 4 nodes are same and leaf we can merge: create one node with val
            if topleft.isLeaf and topright.isLeaf and bottomleft.isLeaf and bottomright.isLeaf and \
                (topleft.val == topright.val == bottomleft.val == bottomright.val):
                return Node(topleft.val, True, None, None, None, None)
            ## else we want to make node with all 4 nodes are return
            return Node(1, False, topleft, topright, bottomleft, bottomright)
        return constructNode(0, len(grid), 0, len(grid[0]))
