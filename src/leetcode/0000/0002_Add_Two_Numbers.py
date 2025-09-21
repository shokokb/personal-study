from typing import Optional
import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def linked_list(l):
        root = ListNode(l[0])
        node = root
        for v in l[1:]:
            node.next = ListNode(v)
            node = node.next
        return root
    @staticmethod
    def to_list(node):
        res = []
        while(node):
            res.append(node.val)
            node = node.next
        return res


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  
        node = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            s = val1 + val2 + carry
            carry = s // 10
            node.next = ListNode(s % 10)
            node = node.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next

class TestSolution(unittest.TestCase):
    def testAddTwoNumbers(self):
        s = Solution()

        node1 = ListNode.linked_list([2,4,3])
        node2 = ListNode.linked_list([5,6,4])
        expected = ListNode.linked_list([7,0,8])
        self.assertEqual(ListNode.to_list(expected),ListNode.to_list(s.addTwoNumbers(node1,node2)))

        node1 = ListNode.linked_list([0])
        node2 = ListNode.linked_list([0])
        expected = ListNode.linked_list([0])
        self.assertEqual(ListNode.to_list(expected),ListNode.to_list(s.addTwoNumbers(node1,node2)))

        node1 = ListNode.linked_list([9,9,9,9,9,9,9])
        node2 = ListNode.linked_list([9,9,9,9])
        expected = ListNode.linked_list([8,9,9,9,0,0,0,1])
        self.assertEqual(ListNode.to_list(expected),ListNode.to_list(s.addTwoNumbers(node1,node2)))

def main():
    unittest.main()

if __name__ == "__main__":
    main()
        