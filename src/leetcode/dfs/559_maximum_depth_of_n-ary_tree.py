# coding : UTF-8

import unittest
from typing import List
from typing import Optional
from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        if not children:
            self.children = []
        else:
            self.children = children

    @staticmethod
    def to_node(values):
        n = len(values) 

        if n == 0:
            return None

        root = Node(values[0])
        queue = deque([root])

        parent = None        
        children_values = []
        for val in values[1:]:
            if val is None:
                parent = queue.popleft()
            else:
                c = Node(val)
                queue.append(c)
                parent.children.append(c)
                # print("DEBUG", parent.val, [c.val for c in parent.children])
        return root

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # if root is None:
        #     return 0
        # if not root.children:
        #     return 1
        # # print("[DEBUG]:", root.val, [c.val for c in root.children])
        # return max([self.maxDepth(c) for c in root.children])+1
        if root is None:
            return 0

        stack = [(root, 1)]
        max_depth = 0

        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            for c in node.children:
                stack.append((c, depth+1))
        return max_depth

class TestSolution(unittest.TestCase):
    def testMaxDepth(self):
        s = Solution()

        n = Node.to_node([1,None,3,2,4,None,5,6])
        self.assertEqual(3, s.maxDepth(n))

        n = Node.to_node([1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14])
        self.assertEqual(5, s.maxDepth(n))

        n = Node.to_node([])
        self.assertEqual(0, s.maxDepth(n))

def main():
    unittest.main()

if __name__ == "__main__":
    main()