# coding : UTF-8

import unittest
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Basic Greedy
        # res = 0
        # for c in coins[::-1]:
        #     res += amount // c
        #     amount = amount % c
        # return res if amount == 0 else -1
        
        # DP
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            dp[i] = min((dp[i-c]+1 for c in coins if i >= c), default=float('inf'))
        # print(dp)
        return dp[amount] if dp[amount] != float('inf') else -1
        
class TestSolution(unittest.TestCase):
    def testCoinChange(self):
        s = Solution()
        self.assertEqual(3, s.coinChange([1,2,5], 11))
        self.assertEqual(-1, s.coinChange([2], 3))
        self.assertEqual(0, s.coinChange([1], 0))
        self.assertEqual(2, s.coinChange([1,3,4], 6))

def main():
    unittest.main()

if __name__ == "__main__":
    main()