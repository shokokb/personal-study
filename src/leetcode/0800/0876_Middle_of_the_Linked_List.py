# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        def depth(root) -> int:
            if not root: return 0
            return depth(root.next) + 1
        max_depth = depth(head)
        mid_depth = (max_depth + 1) // 2 if max_depth % 2 == 1 else max_depth // 2
        d = max_depth
        while head:
            if d == mid_depth:
                return head
            head = head.next