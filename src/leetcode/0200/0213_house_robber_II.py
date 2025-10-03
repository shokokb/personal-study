# coding : UTF-8

import unittest
from typing import List

class Solution:
    def rob_part(self, nums: List[int], start, end):        
        prev2, prev1 = 0, 0
        for i in range(start, end+1):
            curr = max(prev2+nums[i], prev1)
            prev2, prev1 = prev1, curr
        return prev1

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self.rob_part(nums, 0, n-2), self.rob_part(nums, 1, n-1))

class TestSolution(unittest.TestCase):
    def testRob(self):
        s = Solution()
        self.assertEqual(3,s.rob([2,3,2]))
        self.assertEqual(4,s.rob([1,2,3,1]))
        self.assertEqual(3,s.rob([1,2,3]))
        self.assertEqual(1,s.rob([1]))

def main():
    unittest.main()

if __name__ == "__main__":
    main()
