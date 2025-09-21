class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        cnt = collections.Counter(nums)
        ret = []
        for k, c in cnt.items():
            if c >= 2:
                ret.append(k)
        return ret