class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums = list(filter(lambda x: x < k, nums))
        nums.sort(reverse=True)
        sumv = -1
        for i, n in enumerate(nums):
            for j, m in enumerate(nums[i+1:]):
                if n + m >= k:
                    pass
                elif n + m > sumv:
                    sumv = n + m
                    break
                else:
                    break
        return sumv