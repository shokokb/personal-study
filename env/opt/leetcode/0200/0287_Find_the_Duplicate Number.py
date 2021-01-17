class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # c = collections.Counter(nums)
        # for n, cnt in c.items():
        #     if cnt > 1:
        #         return n
        seen = set()
        for n in nums:
            if n in seen:
                return n
            seen.add(n)