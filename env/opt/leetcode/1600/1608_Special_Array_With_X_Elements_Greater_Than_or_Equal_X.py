class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        for x in range(n + 1):
            l = list(filter(lambda a: a >= x, nums))
            if x == len(l):
                return x
        return -1