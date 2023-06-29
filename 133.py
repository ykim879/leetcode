"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # visited: keeps track of visited
        # bfs: store neighbor 
        # dictionary of node.val: node
        if not node:
            return None
        nodes = {}
        q = deque([node])
        visited = set()
        while q:
            cur = q.popleft()
            if cur and cur.val not in visited:
                visited.add(cur.val)
                curClone = nodes.get(cur.val, Node(cur.val))
                if curClone.val not in nodes:
                    nodes[cur.val] = curClone
                for neighbor in cur.neighbors:
                    neighborClone = nodes.get(neighbor.val, Node(neighbor.val))
                    if  neighborClone.val not in nodes:
                        nodes[neighbor.val] = neighborClone
                    curClone.neighbors.append(neighborClone)
                    if neighborClone.val not in visited:
                        q.append(neighbor)
        return nodes[node.val]
