class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        nums = [0, 1]
        for i in range(1, n // 2 + 1):
            nums.append(nums[i])
            nums.append(nums[i] + nums[i + 1])
        # print(nums[:n+1])
        return max(nums[:n+1])