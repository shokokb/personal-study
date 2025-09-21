class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        nums = list(filter(lambda x: x > 0, nums))
        num = 1
        while True:
            if num not in nums:
                return num
            num += 1
        