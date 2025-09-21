class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = defaultdict(lambda:False)
        for n in nums:
            if d[n]:
                return n
            d[n] = True