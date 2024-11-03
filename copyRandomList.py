"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # dict : key = org and value = newnode
        d = {}
        ## by traversing head -> interwine the next (if next is already exited, it is created by random)
        ## and for random: (if random already existed it was populated by next)
        cur = head
        while cur:
            if cur not in d:
                d[cur] = Node(cur.val)
            if cur.next:
                if cur.next not in d:
                    d[cur.next] = Node(cur.next.val)
                d[cur].next = d[cur.next]
            if cur.random:
                if cur.random not in d:
                    d[cur.random] = Node(cur.random.val)
                d[cur].random = d[cur.random]
            cur = cur.next
        return d[head]
