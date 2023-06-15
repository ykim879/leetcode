# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not k:
            return head
        # no change required
        length = 0
        tail = None
        prev = None
        current = head
        while current:
            length += 1
            if not current.next:
                tail = current
            current = current.next
        k %= length
        if k == 0:
            return head
        k = (length - k)
        # find prev
        current = head
        while k:
            if k == 1:
                prev = current
            current = current.next
            k -= 1
        tail.next = head
        current = prev.next
        prev.next = None
        return current

        
        
