# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        i = 0
        ret = head
        while head:
            i += 1
            if i == m:
                ptr = head
                for j in range(n):
                    if ptr is not None:
                        ptr = ptr.next
                if ptr is not None:
                    head.next = ptr.next
                else:
                    head.next = None
                i = 0
            head = head.next
        return ret
    
            
        
        