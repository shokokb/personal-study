# 頭頂部に最小値が来るヒープ
class Heap:
    def __init__(self):
        self.heap = []

    def add(self, v):
        self.heap.append(v)
        n = len(self.heap) - 1
        p = (n - 1) // 2
        while n > 0:
            # 親が自分より小さければ抜ける
            if self.heap[p] <= self.heap[n]:
                break
            else:
                self.heap[n], self.heap[p]  = self.heap[p], self.heap[n]
            n = p  # p

    def remove(self):
        if len(self.heap) == 1:
            return self.heap[0]
        min = self.heap[0]
        last = self.heap.pop()
        self.heap[0] = last
        n = 0
        while n < len(self.heap):
            cn = 2 * n + 1 # 左側の子
            cr = 2 * n + 2  # 右側の子
            if cr < len(self.heap):
                c = self.heap[cn]  
                r = self.heap[cr]
                if r < c:       # 右の子の方が小さい場合
                    cn = cr
                    c = r
            elif cn < len(self.heap):
                c = self.heap[cn]  
            else:
                break
            if c < last:
                self.heap[n], self.heap[cn] = self.heap[cn], self.heap[n]
            else:
                break
            n = cn
        return min

    def sort(list):
        h = Heap()
        for n in list:
            h.add(n)
        print(h.heap)

        ans = []
        for n in list:
            ans.append(h.remove())
        return ans

            
if __name__ == "__main__":
    ans = Heap.sort([1, 3, 6, 4, 8, 7, 5])
    print(ans)
    ans = Heap.sort([2, 7, 11, 15])
    print(ans)
