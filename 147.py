# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        insertion, sortedList = head.next, ListNode(0, head)
        head.next = None
        while insertion:
            insertedTo = sortedList
            while insertedTo.next and insertedTo.next.val < insertion.val:
                insertedTo = insertedTo.next
            # insert
            nex = insertedTo.next
            insertedTo.next = insertion
            insertion = insertion.next
            insertedTo.next.next = nex
        return sortedList.next
