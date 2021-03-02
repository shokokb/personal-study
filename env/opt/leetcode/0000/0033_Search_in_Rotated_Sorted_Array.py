class Solution:
    def findMin(self, nums: List[int]) -> int:
        def find_rotated_index(left:int, right:int) -> int:
            if nums[left] < nums[right]:
                return 0
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] > nums[pivot + 1]:
                    return pivot + 1
                else:
                    if nums[left] > nums[pivot]:
                        right = pivot - 1
                    else:
                        left = pivot + 1
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        rotated_index = find_rotated_index(0, n - 1)
        # print(rotated_index)
        return nums[rotated_index]