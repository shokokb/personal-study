# coding : UTF-8

from typing import List
import unittest

# Time complexity : O(n)
# Space complexity : O(n)->O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)

        # O(1)
        prev1, prev2 = 0,0
        for num in nums:
            current = max(prev1, prev2 + num)
            prev2, prev1 = prev1, current
        return prev1

        # dp = [0] * n
        # for i in range(n):
        #     prev1 = dp[i-1] if i >= 1 else 0
        #     prev2 = (dp[i-2] if i >= 2 else 0)+nums[i]
        #     dp[i] = max(prev1, prev2)

        # return dp[n-1]

class TestSolution(unittest.TestCase):
    def testRob(self):
        s = Solution()
        self.assertEqual(4,s.rob([1,2,3,1]))

def main():
    unittest.main()

if __name__ == "__main__":
    main()