# coding : UTF-8

import unittest
from collections import deque

class TreeNode:
    def __init__ (self, val, left = None, right = None):
        self.val = val
        self.left = left 
        self.right = right
    
    @staticmethod
    def max_depth(node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return 1 + max(TreeNode.max_depth(node.left), TreeNode.max_depth(node.right))
    
    @staticmethod
    def list_to_treenode(values):
        if not values:
            return None

        i = 0
        root = TreeNode(values[0])
        queue = deque([root])

        while queue and i < len(values):
            parent = queue.popleft()
            i += 1 
            if i < len(values) and values[i] is not None:
                parent.left = TreeNode(values[i])
                queue.append(parent.left)
            i += 1 
            if i < len(values) and values[i] is not None:
                parent.right = TreeNode(values[i])
                queue.append(parent.right)
        return root
    
    @staticmethod
    def preorder(node):
        if node is None:
            return []
        return [node.val] + TreeNode.preorder(node.left) + TreeNode.preorder(node.right)
    
    @staticmethod
    def inorder(node):
        if node is None:
            return []
        return TreeNode.inorder(node.left) + [node.val] + TreeNode.inorder(node.right)
    
    @staticmethod
    def postorder(node):
        if node is None:
            return []
        return TreeNode.postorder(node.left) + TreeNode.postorder(node.right) + [node.val] 

class TestTreeNode(unittest.TestCase):
    def testDepth(self):
        root = TreeNode.list_to_treenode([1,2,3,4,5,6,7,None,9,10])
        self.assertEqual(4, TreeNode.max_depth(root))

    def testPreorder(self):
        root = TreeNode.list_to_treenode([1,2,3,4,5,6,7,None,9,10])
        self.assertEqual([1, 2, 4, 9, 5, 10, 3, 6, 7], TreeNode.preorder(root))

    def testInorder(self):
        root = TreeNode.list_to_treenode([1,2,3,4,5,6,7,None,9,10])
        self.assertEqual([4, 9, 2, 10, 5, 1, 6, 3, 7], TreeNode.inorder(root))

    def testPostorder(self):
        root = TreeNode.list_to_treenode([1,2,3,4,5,6,7,None,9,10])
        self.assertEqual([9, 4, 10, 5, 2, 6, 7, 3, 1], TreeNode.postorder(root))

def main():
    unittest.main()

if __name__ == "__main__":
    main()