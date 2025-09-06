# coding : UTF-8

import unittest

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # # Time Complexity = O(mn)
        # # Space Complexity = O(mn)
        # n, m = len(text1), len(text2)
        # dp = [[0] * (m+1) for _ in range(n+1)]
        # for i in range(1, n+1):
        #     for j in range(1, m+1):
        #         if text1[i-1] == text2[j-1]:
        #             dp[i][j] = dp[i-1][j-1]+1
        #         else:
        #             dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # # print(dp)
        # return dp[n][m]

        # # Time Complexity = O(mn)
        # # Space Complexity = O(m) dp[2][0...m]
        n, m = len(text1), len(text2)
        prev = [0] * (m+1) # dp[i-1]
        curr = [0] * (m+1) # dp[i]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    curr[j] = prev[j-1] + 1
                else:
                    curr[j] = max(prev[j], curr[j-1])
            prev, curr = curr, [0] * (m+1)
        return prev[m]

        # Time Complexity = O(mn)
        # Space Complexity = O(m) 1D array
        # n, m = len(text1), len(text2)
        # dp = [0] * (2*(m+1))  # prev + curr

        # for i in range(1, n+1):
        #     for j in range(1, m+1):
        #         if text1[i-1] == text2[j-1]:
        #             dp[m+1 + j] = dp[j-1] + 1   # 左上 +1
        #         else:
        #             dp[m+1 + j] = max(dp[j], dp[m+1 + j - 1])  # 上 or 左
        #     # copy curr -> prev
        #     dp[:m+1] = dp[m+1:2*(m+1)]
        #     # reset curr
        #     dp[m+1:] = [0]*(m+1)

        # return dp[m]  # ← prev[m] を返す

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