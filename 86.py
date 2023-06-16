# beats 98%
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head
        smaller_head =smaller_tail= ListNode() #dummy node
        bigger_head = bigger_tail = ListNode()
        current = head
        while current:
            if current.val < x:
                smaller_tail.next = current
                current = current.next
                smaller_tail = smaller_tail.next
                smaller_tail.next = None
            else:
                bigger_tail.next = current
                current = current.next
                bigger_tail = bigger_tail.next
                bigger_tail.next = None
        smaller_tail.next = bigger_head.next
        return smaller_head.next
