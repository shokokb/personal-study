class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-1, -1, -1):
            if nums[:i].count(nums[i]) > 0:
                nums.pop(i)
        return len(nums)