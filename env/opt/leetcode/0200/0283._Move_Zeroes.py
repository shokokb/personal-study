class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = []
        for i, n in enumerate(nums):
            if n == 0:
                zeros.append(i)
        zeros.sort(reverse=True)
        for i in zeros:
            n = nums.pop(i)
            nums.append(n)