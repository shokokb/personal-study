# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        node = list1
        node_prev_a = None
        node_next_b = None
        i = 0
        while node:
            i += 1
            if i == a:
                node_prev_a = node
            if i == b + 1:
                node_next_b = node.next
                break
            node = node.next
        node_prev_a.next = list2
        node = list2
        while node:
            if node.next is None:
                node.next = node_next_b
                break
            node = node.next
        return list1