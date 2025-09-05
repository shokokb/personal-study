# coding : UTF-8

import unittest
from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def list_to_tree(arr):
        if not arr:
            return None

        root = TreeNode(arr[0])
        queue = deque([root])
        i = 1
        while queue and i < len(arr):
            parent_node = queue.popleft()
            if arr[i] is not None:
                parent_node.left = TreeNode(arr[i])
                queue.append(parent_node.left)
            i += 1
            if i < len(arr) and arr[i] is not None:
                parent_node.right = TreeNode(arr[i])
                queue.append(parent_node.right)
            i += 1
        return root

class Solution:
    # Time Complaxity  = O(n) 
    # Space Complexity = O(h)
    #                    O(n) in the worst case
    # n = node count, h = tree depth 
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

class TestSolution(unittest.TestCase):
    def testMaxDepth(self):
        s = Solution()
        self.assertEqual(3, s.maxDepth(TreeNode.list_to_tree([3,9,20,None,None,15,7])))

def main():
    unittest.main()

if __name__ == "__main__":
    main()