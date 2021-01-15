# coding: UTF-8

from collections import deque


# class TreeNode:
#     @classmethod
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BinaryTree:
    @classmethod
    def __init__(self):
        self.l = [None for i in range(50)]

    @classmethod
    def insert(self, val):
        if self.l[0] is None:
            self.l[0] = val
            return
        
        i = 1
        li = 2 * i
        ri = 2 * i + 1
        while i <= len(self.l):
            if val < self.l[i-1]:
                if self.l[li-1] is None:
                    self.l[li-1] = val
                    return 
                i = li
            else:
                if self.l[ri-1] is None:
                    self.l[ri-1] = val
                    return
                i = ri
            li = 2 * i
            ri = 2 * i + 1

    @classmethod
    def remove(self, val):
        if self.l[0] is None:
            return None

        i = 1
        li = 2 * i
        ri = 2 * i + 1

        while i <= len(self.l):
            if self.l[i-1] == val:
                print("found", i, self.l[i-1])

                # 左ノードが存在する場合は、左ノードの最大値を探索して、格納する
                if self.l[li-1] is not None:
                    j = li
                    while self.l[j-1]:
                        jr = 2 * j + 1
                        if self.l[jr-1] is None:
                            break
                        j = jr
                    self.l[i-1] = self.l[j-1]
                    self.l[j-1] = None
                    print("node", j, self.l[j-1])
                    return
                
                # 右ノードが存在する場合は、右ノードの最小値を探索して、格納する
                if self.l[ri-1] is not None:
                    j = ri
                    while self.l[j-1]:
                        jl = 2 * j
                        if self.l[jl-1] is None:
                            break
                        j = jl
                    self.l[i-1] = self.l[j-1]
                    self.l[j-1] = None
                    return

                # どちらも存在しない場合は、Noneに設定する
                self.l[i-1] = None
                return


                # return

            if val < self.l[i-1]:
                i = li
            else:
                i = ri

            li = 2 * i
            ri = 2 * i + 1
    
    @classmethod
    def search(self, val):
        if self.l[0] is None:
            return None

        i = 1
        li = 2 * i
        ri = 2 * i + 1
        while True:
            if self.l[i-1] is None:
                return None
            
            if val == self.l[i-1]:
                return self.l[i-1]

            if val < self.l[i-1]:
                i = li
            else:
                i = ri
            li = 2 * i
            ri = 2 * i + 1


    @classmethod
    def display(self):
        d = 1
        dn = 2 ** (d-1)
        arr = []
        for i, n in enumerate(self.l):
            arr.append(n)
            if i == dn - 1:
                print(arr)
                arr.clear()
                d += 1
                dn += 2 ** (d - 1) 
        print(arr)
        print("======")

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

if __name__ == "__main__":
    bt = BinaryTree()
    
    bt.insert(15)
    bt.insert(9)
    bt.insert(23)
    bt.insert(3)
    bt.insert(12)
    bt.insert(17)
    bt.insert(28)
    bt.insert(1)
    bt.insert(8)
    bt.display()

    bt.insert(4)
    bt.display()

    bt.remove(28)
    bt.display()

    bt.remove(8)
    bt.display()

    bt.remove(9)
    bt.display()

    n = bt.search(12)
    print(n)