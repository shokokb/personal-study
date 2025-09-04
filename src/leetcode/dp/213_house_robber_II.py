# coding : UTF-8

import unittest
from typing import List

class Solution:
    def rob_part(self, nums: List[int]):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        # dp = [0] * n
        # dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        # for i in range(2, n):
        #     dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        # return dp[-1]
        prev2, prev1 = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            curr = max(prev2+nums[i], prev1)
            prev2, prev1 = prev1, curr
        return prev1

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left  = self.rob_part(nums[:-1])
        right = self.rob_part(nums[1:])
        return max(left, right)

class TestSolution(unittest.TestCase):
    def testRob(self):
        s = Solution()
        self.assertEqual(3,s.rob([2,3,2]))
        self.assertEqual(4,s.rob([1,2,3,1]))
        self.assertEqual(3,s.rob([1,2,3]))
        self.assertEqual(1,s.rob([1]))

def main():
    unittest.main()

if __name__ == "__main__":
    main()
