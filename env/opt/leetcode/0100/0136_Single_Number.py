class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        for key, cnt in c.items():
            if cnt == 1:
                return key
        return 