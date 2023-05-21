# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        start = dummy = ListNode(0, head)
        #find start
        for i in range(left - 1):
            start = start.next
        #reverse
        if not start or not start.next or not start.next.next:
            return head
        prev = start.next
        cur = prev.next
        nex = cur.next
        for i in range(left, right):
            cur.next = prev
            prev = cur
            cur = nex
            if not nex:
                break
            nex = nex.next
        if start.next:
            start.next.next = cur
        start.next = prev
        return dummy.next
