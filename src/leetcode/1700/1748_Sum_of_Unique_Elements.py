class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        cnt = collections.Counter(nums)
        return sum([num for num, c in cnt.items() if c == 1])
        