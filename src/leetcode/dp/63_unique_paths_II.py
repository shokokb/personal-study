# coding : UTF-8

import unittest
from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Time Complexity = O(m*n)
        # Space Complexity = O(m*n)
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]
        # print(dp)

        dp[0][0] = 0 if obstacleGrid[0][0] == 1 else 1
        for j in range(1, n):
            dp[0][j] = 0 if obstacleGrid[0][j] == 1 else dp[0][j-1]

        for i in range(1,m):
            dp[i][0] = 0 if obstacleGrid[i][0] == 1 else dp[i-1][0]

            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # print(dp)

        return dp[-1][-1]

        # Time Complexity = O(m*n)
        # Space Complexity = O(n)
        # m = len(obstacleGrid)
        # n = len(obstacleGrid[0])

        # dp = [0] * n
        # # print(dp)

        # dp[0] = 1
        # for j in range(1,n):
        #     if obstacleGrid[0][j] == 1 or dp[j-1] == 0:
        #         dp[j] = 0
        #     else:
        #         dp[j] = 1
        # # print(dp)

        # for i in range(1,m):
        #     dp[0] = 0 if obstacleGrid[i][0] == 1 else 1
        #     for j in range(1,n):
        #         if obstacleGrid[i][j] == 1:
        #             dp[j] = 0
        #         else:
        #             dp[j] += dp[j-1]
        # # print(dp)

        # return dp[-1]

class TestSolution(unittest.TestCase):
    def testUniquePathsWithObstacles(self):
        s = Solution()
        self.assertEqual(2, s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
        self.assertEqual(1, s.uniquePathsWithObstacles([[0,1],[0,0]]))

def main():
    unittest.main()

if __name__ == "__main__":
    main()