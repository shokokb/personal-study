# coding : UTF-8

import unittest

class Solution:
    # Time Complexity = O(mn)
    # Space Complexity = O(mn)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # print(dp)
        return dp[n][m]
        # TODO : 2D array -> 1D array

class TestSolution(unittest.TestCase):
    def testLongestCommonSubsequence(self):
        s = Solution()
        self.assertEqual(3, s.longestCommonSubsequence("abcde", "ace"))
        self.assertEqual(3, s.longestCommonSubsequence("abc", "abc"))
        self.assertEqual(0, s.longestCommonSubsequence("abc", "def" ))

def main():
    unittest.main()

if __name__ == "__main__":
    main()