class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        m = max(nums)
        for n in range(0, m + 1):
            if c[n] == 0:
                return n
        return m + 1