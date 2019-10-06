# 頭頂部に最小値が来るヒープ
class Heap:
    def __init__(self):
        self.data = []

    # ながさ
    def len(self):
        return len(self.data)

    # 深さ
    def depth(self):
        i = 1
        depth = 0
        while (i <= len(self.data)):
           i = i * 2
           depth += 1
        return depth
    
    # 親ノードの添字
    def p(c):
        return (c - 1) // 2
    
    # 左側の子ノードの添字
    def cl(p):
        return 2 * p + 1
    
    # 右側の子ノードの添字
    def cr(p):
        return 2 * (p + 1)
    
    # 追加
    def heapup(self, val):
        self.data.append(int(val))
        n = self.len() - 1
        while n > 1:
            p = Heap.p(n)
            if (self.data[p] > self.data[n]):
                self.data[p], self.data[n] = self.data[n], self.data[p]
            else:
                break
            n = n // 2

    def heapdown(self):
        ret = self.data[0]
        self.data[0] = self.data.pop()
        p = 0
        # 現在のノードがRangeOverしない限り
        while (p < self.len() - 1):
            cl = Heap.cl(p)
            cr = Heap.cr(p)
            # 右側の子ノードがある場合
            if cr < self.len():
                if self.data[cr] < self.data[cl]:
                    c = cr
                else:
                    c = cl
            # 左側の子ノードがある場合
            elif cl < self.len():
                c = cl
            # そのほかの場合
            else:
                return

            if c < self.data[p]:
                self.data[c], self.data[p] = self.data[p], self.data[c]
                p = c
            else:
                return
        return

    # ヒープソート
    def sort(self):
        sorted = []
        while self.len() > 1:
            sorted.append(self.data[0])
            self.heapdown()
        if self.len() == 1:
            sorted.append(self.data[0])
        return sorted

    # 標準出力
    def print(self):
        for n in self.data:
            print(str(n) + " ", end="")
        print("")
    
            
if __name__ == "__main__":
    h = Heap()
    h.heapup(1)
    h.heapup(3)
    h.heapup(6)
    h.heapup(4)
    h.heapup(8)
    h.heapup(7)
    h.heapup(5)
    # h.print()
    print(h.sort())
    # print(Heap.p(1) == 0)
    # print(Heap.p(2) == 0)
    # print(Heap.p(9) == 4)
    # print(Heap.p(12) == 5)
    # print(Heap.cl(3) == 7)
    # print(Heap.cl(3) == 8)