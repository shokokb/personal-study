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
    
    def search(self, node:Node, value:int) -> bool:
        if node is None:
            return "no"
        if node.value == value:
            return "yes"
        if value <= node.value:
            return self.search(node.left, value)
        return self.search(node.right, value)
    
    def delete(self, value:int) -> bool:
        parent = None
        side = ""
        node = self.root
        while True:
            if node is None:
                break
            if value == node.value:
                break
            elif value < node.value:
                parent = node
                side = "left"
                node = node.left
            else:
                parent = node
                side = "right"
                node = node.right
        # print("parent", parent)
        # print("node", node)
        # print("side", side)
        if node.left is None and node.right is None:
            if side == "left":
                parent.left = None
            else:
                parent.right = None
        elif node.left is None:
            if side == "left":
                parent.left = None
            else:
                parent.right = None
        elif node.right is None:
            if side == "left":
                parent.left = None
            else:
                parent.right = None
        else:
            tmp = self.delete_min(node)
            print("node", node)
            print("tmp", tmp)
    
    def delete_min(self, node:Node):
        node = node.right
        print("right", node)
        while node.left is not None:
            node = node.left
        return node

tree = BinarySearchTree(7)
tree.insert(10)
tree.insert(12)
tree.insert(5)
tree.insert(7)
tree.insert(8)
print("===")
tree.inorder(tree.root)
print("===")
print(tree.search(tree.root, 5))
print(tree.search(tree.root, 11))
print("===")
print(tree.delete(10))
