class Solution:
    def isArmstrong(self, N: int) -> bool:
        nums = [int(n) for n in str(N)]
        digit = len(nums)
        sumv = 0
        for n in nums:
            sumv += (n % 10) ** digit
        return N == sumv