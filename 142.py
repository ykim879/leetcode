class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        i = 0
        while head and head not in visited:
            visited.add(head)
            head = head.next
        return head
