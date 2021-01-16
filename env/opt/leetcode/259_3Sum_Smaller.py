class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        cnt = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] < target:
                        # print([nums[i], nums[j], nums[k]])
                        cnt += 1
        return cnt