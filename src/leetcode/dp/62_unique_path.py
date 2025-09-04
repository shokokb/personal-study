import math 
import unittest

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Time complaxity : O(m+n)
        # Space complexity : O(1)
        # return math.factorial(m+n-2) // (math.factorial(m-1) * math.factorial(n-1))

        # Time Complexity : O(n*m)
        # Space Complexity : O(m*n)
        # dp = [[0] * m for _ in range(n)]
        # dp[0] = [1] * m
        # for i in range(n):
        #     dp[i][0] = 1
        # for i in range(1,n):
        #     for j in range(1,m):
        #         dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # return dp[-1][-1]

        # Time Complexity : O(n*m)
        # Space Complexity : O(m)
        # prev = [1] * m
        # curr = [0] * m
        # for i in range(1,n):
        #     for j in range(m):
        #         if j == 0:
        #             curr[j] = 1
        #         else :
        #             curr[j] = prev[j] + curr[j-1]
        #     prev = curr
        # return prev[-1]
        dp = [1]*m
        for i in range(1,n):
            for j in range(1,m):
                dp[j] += dp[j-1]
        return dp[-1]

class TestSolution(unittest.TestCase):
    def testUniquePaths(self):
        s = Solution()
        self.assertEqual(28,s.uniquePaths(7,3))
        self.assertEqual(3,s.uniquePaths(3,2))

def main():
    unittest.main()

if __name__ == "__main__":
    main()