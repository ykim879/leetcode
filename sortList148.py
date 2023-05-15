import heapq
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        h = []
        # push in heap
        while head:
            heapq.heappush(h, (head.val, head))
            head = head.next
        # pop in heap
        _, res = heapq.heappop(h)
        cur = res
        while h:
            _, cur.next = heapq.heappop(h)
            cur = cur.next
        cur.next = None
        return res
