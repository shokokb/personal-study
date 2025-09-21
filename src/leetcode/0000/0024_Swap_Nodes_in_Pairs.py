# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        hhead = ListNode(-1)
        hhead.next = head
        node = hhead
        prev = hhead
        left = None
        right = None
        while prev:
            if prev.next is None:
                break
            left = prev.next
            if prev.next.next is None:
                break
            right = prev.next.next
            left.next = right.next
            right.next = left
            prev.next = right
            prev = prev.next.next
        return hhead.next
        