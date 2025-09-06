# coding : UTF-8

from typing import List
import unittest

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # dp = [[0] * n for _ in range(m)]
        # # print(dp)

        # dp[0][0] = grid[0][0]
        # for j in range(1, n):
        #     dp[0][j] = dp[0][j-1] + grid[0][j]

        # for i in range(1, m):
        #     dp[i][0] = dp[i-1][0]+grid[i][0]
        #     for j in range(1, n):
        #         dp[i][j] = min(dp[i-1][j]+grid[i][j], dp[i][j-1]+grid[i][j])
        # # print(dp)

        # return dp[-1][-1]

        dp = [0] * n
        dp[0] = grid[0][0]
        for j in range(1, n):
            dp[j] = dp[j-1] + grid[0][j]
        for i in range(1, m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j-1]) +grid[i][j]
        # print(dp)
        return dp[-1]

class TestSolution(unittest.TestCase):
    def testMinPathSum(self):
        s = Solution()
        self.assertEqual(7, s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))

def main():
    unittest.main()

if __name__ == "__main__":
    main()