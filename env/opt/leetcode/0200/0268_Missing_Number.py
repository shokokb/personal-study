class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mv_value = min(nums)    #O(n)
        max_value = max(nums)   #O(n)
        set_original = set(nums)
        set_range = set(range(0, max_value + 1))
        # print(set_original)
        # print(set_range)
        set_n = set_range - set_original
        if len(set_n) == 0:
            return max_value + 1
        else:
            n = set_n.pop()
            return n