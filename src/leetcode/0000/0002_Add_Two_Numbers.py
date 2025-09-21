# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1, n2 = l1.val, l2.val
        n = (n1 + n2) % 10
        carry = (n1 + n2) // 10
        head = node = ListNode(n)
        # print(n1, n2, n, carry)
        l1 = l1.next
        l2 = l2.next
        
        while l1 or l2 or carry:
            n1, n2 = 0, 0
            if l1:
                n1 = l1.val
                l1 = l1.next
            if l2:
                n2 = l2.val
                l2 = l2.next
            
            n = (n1 + n2 + carry) % 10
            carry = (n1 + n2 + carry) // 10
            # print(n1, n2, n, carry)

            node.next = ListNode(n)
            node = node.next
            
        return head