# coding : UTF-8

import unittest
from collections import deque

class Node:
    def __init__(self, val, children = None):
        self.val = val
        if not children:
            self.children = []
        else:
            self.children = children
    
    # n = node count
    # Time  Complexity = O(n) 
    # Space Complexity = O(n)
    @staticmethod    
    def to_node(values):
        n = len(values) 

        if n == 0:
            return None

        root = Node(values[0])
        queue = deque([root])

        parent = None        
        for val in values[1:]:
            if val is None:
                parent = queue.popleft()
            else:
                c = Node(val)
                queue.append(c)
                parent.children.append(c)
                # print("DEBUG", parent.val, [c.val for c in parent.children])
        return root

    # Time Complexity : O(n)
    # Space Complexity: O(n)
    @staticmethod
    def maxDepth(root: 'Node') -> int:
        if root is None: # Base case
            return 0

        queue = deque([root])
        depth = 0
        while queue:
            depth += 1
            for _ in range(len(queue)):
                n = queue.popleft()
                queue.extend(n.children)
        return depth

class TestNode(unittest.TestCase):
    def testMaxDepth(self):
        n = Node.to_node([1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14])
        self.assertEqual(5, Node.maxDepth(n))
        n = Node.to_node([])
        self.assertEqual(0, Node.maxDepth(n))

def main():
    unittest.main()

if __name__ == "__main__":
    main()