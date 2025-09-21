class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = 0
        # O(nlogn)
        nums.sort()
        
        # O(n)
        l_i = 0
        r_i = len(nums) - 1
        while nums[r_i] >= k and r_i >= 0:
            r_i -= 1
        
        # O(n)
        while l_i < r_i:
            s = nums[l_i] + nums[r_i]
            if s == k:
                l_i += 1
                r_i -= 1
                cnt += 1
            elif s > k:
                r_i -= 1
            else:
                l_i += 1
        
        return cnt