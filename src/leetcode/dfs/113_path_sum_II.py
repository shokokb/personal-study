#coding : UTF-8

from typing import List
from typing import Optional
from collections import deque 
import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    @staticmethod
    def toNode(values):
        if not values:
            return None

        root = TreeNode(values[0])
        queue = deque([root])

        i = 1
        while i < len(values):
            n = queue.popleft()

            if values[i] is not None:
                n.left = TreeNode(values[i])
                queue.append(n.left)
            i += 1

            if i < len(values) and values[i] is not None: 
                n.right = TreeNode(values[i])
                queue.append((n.right))
            i += 1

        return root

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        
        res = []

        stack = [(root,[root.val],root.val)]
        while stack:
            node, path, s = stack.pop()
            if node.left is None and node.right is None and s == targetSum:
                res.append(path)
            if node.left:
                stack.append((node.left, path+[node.left.val], s+node.left.val))
            if node.right:
                stack.append((node.right, path+[node.right.val], s+node.right.val))

        return res

class TestSolution(unittest.TestCase):
    def testPathSum(self):
        s = Solution()

        n = TreeNode.toNode([])
        self.assertEqual([], s.pathSum(n,5))

        n = TreeNode.toNode([5,4,8,11,None,13,4,7,2,None,None,5,1])
        self.assertEqual([[5,4,11,2],[5,8,4,5]], s.pathSum(n,22))

def main():
    unittest.main()

if __name__ == "__main__":
    main()