# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return head
        prev, mid, end = None, head, head
        while end.next and end.next.next:
            prev = mid
            end = end.next.next
            mid = mid.next
        leftTree, rightTree = None, None
        if prev:
            prev.next = None
            leftTree = self.sortedListToBST(head)
        if mid.next:
            rightTree = self.sortedListToBST(mid.next)
        return TreeNode(mid.val, leftTree, rightTree)
