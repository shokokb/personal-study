class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1
        
        if nums[left] < nums[right]:
            return nums[left]
        
        while left <= right:
            pivot = (left + right) // 2
            # print(pivot, left, right)
            if nums[pivot] > nums[pivot + 1]:
                return nums[pivot + 1]
            
            if nums[pivot - 1] > nums[pivot]:
                return nums[pivot]
            
            if nums[left] > nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
                