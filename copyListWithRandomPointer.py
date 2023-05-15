"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        res = Node(head.val)
        mapper = {head : res}
        # copied next first
        cur = res
        org = head.next
        while org:
            nex = Node(org.val)
            mapper[org] = nex
            cur.next = nex
            cur = nex
            org = org.next

        org = head
        cur = res
        while org:
            if org.random:
                cur.random = mapper[org.random]
            # go next
            cur = cur.next
            org = org.next
        return res
