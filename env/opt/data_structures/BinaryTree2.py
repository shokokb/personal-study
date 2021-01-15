# coding: UTF-8

from collections import deque

class BinaryTree:
    @classmethod
    def __init__(self):
        self.root = None

    @classmethod
    # O(logN)
    def min_node(self):
        if not self.root:
            return None
        n = self.root
        while True:
            if n.left:
                n = n.left
            else:
                return n
        return

    @classmethod
    # Olog(N)
    def max_node(self):
        if not self.root:
            return
        n = self.root
        while True:
            if n.right:
                n = n.right
            else:
                return n
        return

    @classmethod
    # O(logN)
    def insert(self, node):
        # print("insert", node.val)
        if not self.root:
            self.root = node
            return

        p = self.root
        while True:
            if node.val < p.val:
                if p.left:
                    p = p.left
                else:
                    p.left = node
                    node.parent = p
                    return
            else:
                if p.right:
                    p = p.right
                else:
                    p.right = node
                    node.parent = p
                    return

    @classmethod
    # O(logN)
    def search(self, val):
        if not self.root:
            return None
        n = self.root
        while True:
            if n.val == val:
                return n
            if val < n.val:
                if n.left:
                    n = n.left
                else:
                    return None
            else:
                if n.right:
                    n = n.right
                else:
                    return None

    # @classmethod
    def remove(self, val):
        n = self.search(val)
        p = n.parent
        print("parent", n.parent.val)
        if n.left:
            left_max = n.left
            while left_max:
                if left_max.right is None:
                    return left_max
                left_max = left_max.right
            # left_max.left = n.left
            # left_max.right = n.right
            # if n.parent is None:
            #     self.root = n
            # else:
            #     if p.left is n:
            #         p.left = n
            #     else:
            return n
        if n.right:
            right_min = n.right
            while right_min:
                if right_min is None:
                    break
                right_min = right_min.right
            return n
        
        return n

    # @classmethod
    # def sort(self):

    @classmethod
    def bfs(self):
        if not self.root:
            return []

        ret = []
        q = deque()
        q.append(self.root)
        while q:
            p = q.popleft()
            ret.append(p.val)
            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)
        return ret


class TreeNode:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def print_value(self):
        print(self.val)


if __name__ == "__main__":
    bt = BinaryTree()

    bt.insert(TreeNode(15))
    bt.insert(TreeNode(9))
    bt.insert(TreeNode(23))
    bt.insert(TreeNode(3))
    bt.insert(TreeNode(12))
    bt.insert(TreeNode(17))
    bt.insert(TreeNode(28))
    bt.insert(TreeNode(1))
    bt.insert(TreeNode(8))
    bt.insert(TreeNode(4))
    print(bt.bfs())

    print("min value")
    print(bt.min_node().val)

    print("max val")
    print(bt.max_node().val)

    print("search")
    n = bt.search(3)
    if n is not None:
        print(n.val)
    else:
        print("not found")

    print("remove")
    n = bt.remove(28)
    if n is not None:
        print("remove", n.val)