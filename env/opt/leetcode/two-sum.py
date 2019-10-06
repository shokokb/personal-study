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
    
            
class Solution:
    def twoSum(self, nums, target):
        return []

if __name__ == "__main__":
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
    nums = [2, 7, 11, 15]
    sol = Solution()
    ans = sol.twoSum(nums, 9)
    print(ans)
