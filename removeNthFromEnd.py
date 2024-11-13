# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # left and right and gap between is n, whenever right pointer is end, remove lefts.next
        dummy = ListNode(0, head)
        left, right = dummy, dummy
        for _ in range(n):
            right = right.next
        # find right nth node
        while right.next:
            right = right.next
            left = left.next
        # remove left.next
        left.next = left.next.next
        return dummy.next
