# coding : UTF-8

import unittest

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val   = val
        self.left  = left
        self.right = right

    # Time Complexity = O(n)
    # Space Complexity = O(h), but O(n) in the worst case
    # h = Tree depth
    @staticmethod
    def count_node (root):
        if not root:
            return 0
        return TreeNode.count_node(root.left)+TreeNode.count_node(root.right)+1

class TestTreeNode(unittest.TestCase):
    def testDepth(self):
        tn = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
        self.assertEqual(5, TreeNode.count_node(tn))

def main():
    unittest.main()

if __name__ == "__main__":
    main()
