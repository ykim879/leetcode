from typing import List, Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Min-heap to track the smallest node among the k lists
        min_heap = []
        
        # Initialize the heap with the first node of each list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        
        # Dummy head to build the merged linked list
        dummy = ListNode()
        current = dummy
        
        # While there are nodes in the heap
        while min_heap:
            # Pop the smallest node from the heap
            val, i, node = heapq.heappop(min_heap)
            
            # Add the node to the merged list
            current.next = node
            current = current.next
            
            # If the node has a next node, push it into the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
        
        return dummy.next
