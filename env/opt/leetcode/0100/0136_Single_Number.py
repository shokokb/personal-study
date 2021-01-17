class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(list(set(nums))) - sum(nums)