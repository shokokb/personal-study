# coding : UTF-8

import unittest

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1) + 1, len(word2) + 1
        dp = [[0]*l1 for _ in range(l2)]
        for i in range(1, l1):
            dp[0][i] = i
        for j in range(1, l2):
            dp[j][0] = j
        for i in range(1, l2):
            for j in range(1, l1):
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(\
                        dp[i-1][j]+1,   # remove
                        dp[i][j-1]+1,   # insert
                        dp[i-1][j-1]+1  # replace
                    )
        # print(dp)
        return dp[-1][-1]

class TestSolution(unittest.TestCase):
    def testMinDistance(self):
        s = Solution()
        self.assertEqual(3, s.minDistance("horse", "ros"))
        self.assertEqual(5, s.minDistance("intention", "execution"))

def main():
    unittest.main()

if __name__ == "__main__":
    main()