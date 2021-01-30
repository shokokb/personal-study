class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums = list(filter(lambda x: x < k, nums))
        combs = combinations(nums, 2)
        sumv = -1
        for comb in combs:
            if sumv < sum(comb) < k:
                sumv = sum(comb)
        return sumv
        