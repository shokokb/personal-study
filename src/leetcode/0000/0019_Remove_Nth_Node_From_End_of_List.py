# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        ptr = head
        while ptr:
            ptr = ptr.next
            length += 1
        i = 0
        left_node_idx = length - n - 1
        
        ptr = head
        idx = length - n - 1
        if idx < 0:
            head = head.next
        else:
            while ptr:
                if i == idx:
                    ptr.next = ptr.next.next
                    break
                ptr = ptr.next
                i += 1
        return head