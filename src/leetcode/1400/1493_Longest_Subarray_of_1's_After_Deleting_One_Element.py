class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        total = []
        l = []
        for i, n in enumerate(nums):
            if i == 0:
                l = [n]
            elif nums[i-1] != nums[i]:
                total.append(l)
                l = [nums[i]]
            else:
                l.append(nums[i])
        total.append(l)
        
        total = [(l[0], len(l)) for l in total]
        print(total)

        NUM = 0
        CNT = 1
        if len(total) == 1 and total[0][NUM] == 1:
            return total[0][CNT] - 1
        
        max_count = 0
        for i, item in enumerate(total):
            if item[NUM] == 1:
                length = item[CNT]
                if length > max_count:
                    max_count = length

        for i, item in enumerate(total[:-2]):
            # print(i, item[NUM], item[CNT])
            if  total[i][NUM]   == 1 and \
                total[i+1][NUM] == 0 and total[i+1][CNT] == 1 and \
                total[i+2][NUM] == 1:
                length = total[i][CNT] + total[i+2][CNT]
                if length > max_count:
                    max_count = length
        return max_count
                