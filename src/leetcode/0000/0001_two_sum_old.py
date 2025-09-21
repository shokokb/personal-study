# 頭頂部に最小値が来るヒープ
class Solution:
    def __init__(self):
        self.heap = []
        self.idxs = []

    def add(self, v):
        self.idxs.append(len(self.heap))
        self.heap.append(v)
        n = len(self.heap) - 1
        p = (n - 1) // 2
        while n > 0:
            # 親が自分より小さければ抜ける
            if self.heap[p] <= self.heap[n]:
                break
            else:
                self.heap[n], self.heap[p] = self.heap[p], self.heap[n]
                self.idxs[n], self.idxs[p] = self.idxs[p], self.idxs[n]
            n = p  # p

    def remove(self):
        if len(self.heap) == 1:
            return self.heap[0], self.idxs[0]
        min = self.heap[0]
        minidx = self.idxs[0]
        last = self.heap.pop()
        last_index = self.idxs.pop()
        self.heap[0] = last
        self.idxs[0] = last_index
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
                self.idxs[n], self.idxs[cn] = self.idxs[cn], self.idxs[n]
            else:
                break
            n = cn
        return min, minidx

    def sort(list):
        h = Solution()
        for n in list:
            h.add(n)

        ans = []
        for n in list:
            m = h.remove()
            ans.append(m)
        return ans

    def twoSum(self, nums, target):
        # ソーティングする
        data = Solution.sort(nums)
        print(data)
        i = 0
        # # target より大きい要素は切る
        # for item in data:
        #     if item[0] > target:
        #         data = data[:i]
        #         break
        #     i += 1
        # print(data)
        # 一致するものを探す
        i = 0
        for item1 in data[i:]:
            for item2 in data[i + 1:]:
                sum = item1[0] + item2[0]
                if sum == target:
                    if item1[1] > item2[1]:
                        return [item2[1], item1[1]]
                    else:
                        return [item1[1], item2[1]]
                elif sum > target:
                    break
            i += 1
        # 一致するものがなければ空のリストを返す
        return []
        
            
if __name__ == "__main__":
    sol = Solution()
    data = sol.twoSum([230,863,916,585,981,404,316,785,88,12,70,435,384,778,887,755,740,337,86,92,325,422,815,650,920,125,277,336,221,847,168,23,677,61,400,136,874,363,394,199,863,997,794,587,124,321,212,957,764,173,314,422,927,783,930,282,306,506,44,926,691,568,68,730,933,737,531,180,414,751,28,546,60,371,493,370,527,387,43,541,13,457,328,227,652,365,430,803,59,858,538,427,583,368,375,173,809,896,370,789], 542)
    print(data)

