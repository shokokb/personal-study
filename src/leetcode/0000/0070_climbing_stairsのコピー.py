# coding : UTF-8

import unittest

# Time complaxity : O(n * len(steps)) = O(n)
# Space complexity : O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [1, 2]

        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1): # O(n * len(steps))
            for s in steps:
                if i - s >= 0:
                    dp[i] += dp[i-s]
        return dp[n]

class TestSolution(unittest.TestCase):
    def testClimbStairs(self):
        s = Solution()
        self.assertEqual(2, s.climbStairs(2))
        self.assertEqual(3, s.climbStairs(3))

def main():
    unittest.main()

if __name__ == "__main__":
    main()