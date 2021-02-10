class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # print(nums)
        sorted_nums = sorted(nums)
        # print(sorted_nums)
        l, r = 0, len(nums) - 1
        while l < len(nums):
            if nums[l] != sorted_nums[l]:
                print(l)
                break
            l += 1
        while r >= 0:
            if nums[r] != sorted_nums[r]:
                print(r)
                break
            r -= 1
        if r >= l:
            return r - l + 1
        else:
            return 0
        