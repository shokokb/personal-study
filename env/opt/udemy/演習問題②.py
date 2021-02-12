class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__ (self, value:int):
        self.root = Node(value)
    def insert(self, value:int):
        node = self.root
        while True:
            if value <= node.value:
                if node.left is None:
                    node.left = Node(value)
                    return
                node = node.left
            else:
                if node.right is None:
                    node.right = Node(value)
                    return
                node = node.right
    def inorder(self, node:Node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.value)
        self.inorder(node.right)

tree = BinarySearchTree(7)
tree.insert(10)
tree.insert(12)
tree.insert(5)
print("===")
tree.inorder(tree.root)
print("===")
