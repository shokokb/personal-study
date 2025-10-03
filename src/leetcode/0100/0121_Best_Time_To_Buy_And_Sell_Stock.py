# coding : UTF-8

from typing import List
import unittest

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time Complaxity = O(n^2)
        # n = len(prices)
        # res = 0
        # for i in range(1, n): # O(n)
        #     left, right =  min(prices[:i]), max(prices[i:]) # O(n)
        #     if right - left > res:
        #         res = right - left
        # return res      
        # Time Complexity = O(n)
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit



class TestSolution(unittest.TestCase):
    def testMaxProfit(self):
        s = Solution()
        self.assertEqual(5, s.maxProfit([7,1,5,3,6,4]))
        self.assertEqual(0, s.maxProfit([7,6,4,3,1]))

def main():
    unittest.main()

if __name__ == "__main__":
    main()