# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 1) find mid and end.
        mid, end = head, head
        while end.next and end.next.next:
            end = end.next.next
            mid = mid.next
        while end.next:
            end = end.next
        # 2) reverse order from mid to end
        prev, nex = mid, mid.next
        mid.next = None
        while nex:
            temp = nex.next
            nex.next = prev
            prev = nex
            nex = temp
        # 3) interwine by doing start to 
        start = head
        while start and end:
            temp1, temp2 = start.next, end.next
            start.next = end
            end.next = temp1
            start, end = temp1, temp2
        return head
