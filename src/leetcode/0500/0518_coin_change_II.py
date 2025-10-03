# coding : UTF-8

import unittest
from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp =[0] * (amount + 1) 

        dp[0] = 1

        for c in coins:
            for i in range(c, amount + 1):
                dp[i] += dp[i-c]
        return dp[amount]
        
class TestSolution(unittest.TestCase):
    def testCoinChange(self):
        s = Solution()
        self.assertEqual(4, s.change(5, [1,2,5]))
        self.assertEqual(0, s.change(3, [2]))
        self.assertEqual(1, s.change(10, [10]))

def main():
    unittest.main()

if __name__ == "__main__":
    main()