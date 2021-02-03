class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        ret = 0
        for i in range(0, len(nums), 2):
            ret += nums[i-1]
        return ret
        