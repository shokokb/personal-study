#coding : UTF-8

from collections import deque

class TreeNode:
    def __init__(self, v=0, left=None, right=None):
        self.v = v
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # O(logn); O(n) in the worst case
    def add(self, v):
        node = TreeNode(v)
        target = self.root
        if self.root is None:
            self.root = node
        else:
            while True:
                if v <= target.v:
                    if target.left is None: 
                        target.left = node
                        break
                    else:
                        target = target.left 
                else:
                    if target.right is None:
                        target.right = node
                        break
                    else:
                        target = target.right
    
    def remove(self, v):
        if self.root is None:
            return None
        
        def _remove(node, v):
            if node is None:
                return None

            if v < node.v:
                node.left = _remove(node.left, v)
            elif v > node.v:
                node.right = _remove(node.right, v)
            else: # node.v == v
                if node.left is None and node.right is None:
                    return None
                elif node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                else:
                    successor = node.right
                    while successor.left:
                        successor = successor.left
                    node.v = successor.v
                    node.right = _remove(node.right, successor.v)

            return node

        self.root = _remove(self.root, v)
    
    def search(self, v):
        target = self.root
        while target:
            if v < target.v:
                target = target.left
            elif v > target.v:
                target = target.right
            else:
                return target
        return None
    
    def to_list(self):
        res = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node:
                res.append(node.v)
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append(None)

        while res and res[-1] is None:
            res.pop()

        return res

def main():
    btree = BinarySearchTree()

    values = [15, 9, 23, 3, 12, 17, 28, 8]
    for v in values:
        btree.add(v)
        print(btree.to_list())

    btree.add(1)
    print(btree.to_list())

    btree.add(4)
    print(btree.to_list())

    btree.remove(28)
    print(btree.to_list())

    print(btree.search(17).v)
    print(btree.search(28))

if __name__ == "__main__":
    main()