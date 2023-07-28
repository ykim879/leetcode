# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        prev = ListNode(head)
        mid = end = head
        while end and end.next:
            end = end.next
            if end:
                end = end.next
            prev = mid
            mid = mid.next
        prev.next = mid.next
        return head
