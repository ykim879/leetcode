# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 0
        # find mid
        mid = end = ListNode(0, head)
        while end.next:
            end = end.next.next
            mid = mid.next
            n += 1
        
        end = mid.next
        mid = mid.next
        while mid:
            temp = mid
            mid = mid.next
            temp.next = end
            end = temp
        
        mid = head
        res = 0
        while n > 0:
            res = max(res, mid.val + end.val)
            end = end.next
            mid = mid.next
            n -= 1
        return res
