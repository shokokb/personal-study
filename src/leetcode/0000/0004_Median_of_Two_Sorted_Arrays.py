class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1
        nums.extend(nums2)
        nums.sort()
        
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n % 2 == 1:
            return nums[n // 2]
        else:
            return (nums[n // 2 - 1]  + nums[n // 2]) / 2
        