from collections import deque
import unittest

class TreeNode:
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
    def preorder(self):
        res = [self.val]
        if self.left:
            res += self.left.preorder()
        if self.right:
            res += self.right.preorder()
        return res

    def inorder(self):
        res = []
        if self.left:
            res += self.left.inorder()
        res += [self.val]
        if self.right:
            res += self.right.inorder()
        return res

    def postorder(self):
        res = []
        if self.left:
            res += self.left.postorder()
        if self.right:
            res += self.right.postorder()
        res += [self.val]
        return res

    @staticmethod   
    def list_to_node (values):
        if not values:
            return None
        
        root = TreeNode(values[0])
        queue = deque([root])

        i = 1
        while i < len(values):
            parent = queue.popleft()
            if i < len(values) and values[i] is not None:
                parent.left = TreeNode(values[i])
                queue.append(parent.left)
            i += 1
            if i < len(values) and values[i] is not None:
                parent.right = TreeNode(values[i])
                queue.append(parent.right)
            i += 1

        return root

class TestTreeNode(unittest.TestCase):
    def testPreOrder(self):
        root = TreeNode.list_to_node([0,1,2,3,4,5,6,None,7])

        self.assertEqual([0,1,3,7,4,2,5,6], root.preorder())

        self.assertEqual([3,7,1,4,0,5,2,6], root.inorder())
        
        self.assertEqual([7,3,4,1,5,6,2,0], root.postorder())

def main():
    unittest.main()

if __name__ == "__main__":
    main()

