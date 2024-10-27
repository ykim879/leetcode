# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def findhalf(cur):
            # find mid doing fast and slow ptr
            slow, fast = cur, cur.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            mid = slow.next 
            slow.next = None
            return mid
        def sort(cur): # return head of node
            if not cur or not cur.next:
                return cur
            mid = findhalf(cur)
            head = ListNode()
            p = head
            first, second = sort(cur), sort(mid)
            while first and second:
                if first.val <= second.val:
                    p.next = first
                    first = first.next
                else:
                    p.next = second
                    second = second.next
                p = p.next
            p.next = first or second
            return head.next
        return sort(head)
