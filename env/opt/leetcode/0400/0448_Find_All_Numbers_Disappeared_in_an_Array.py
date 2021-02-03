class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        s = {n for n in range(1, len(nums) + 1)}
        return list(s - set(nums))