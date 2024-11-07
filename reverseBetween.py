# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        # recursive:
        def recur(cur, right): 
            ## base case: when I found the right node
            if right == 0:
                return cur, cur, cur.next
            ## head, tail, last = recur(cur.next)
            h, tail, last = recur(cur.next, right - 1)
            tail.next = cur
            return h, cur, last
        cur = dummy ## think edge case of n == 1
        for _ in range(left-1):
            cur = cur.next # left link of 
        h, tail, last = recur(cur.next, right - left)
        cur.next = h
        tail.next = last
        return dummy.next
