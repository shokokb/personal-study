# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n = 0
        result = 0
        while l1 or l2:
            n1, n2 = 0, 0
            if l1:
                n1 = l1.val
                l1 = l1.next
            if l2:
                n2 = l2.val
                l2 = l2.next
            result += (n1 + n2) * 10 ** n
            n += 1
        
        head = node = ListNode(result % 10)
        result //= 10
        while result > 0:
            node.next = ListNode(result % 10)
            result //= 10 
            node = node.next
        return head
        
