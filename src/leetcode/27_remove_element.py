# coding : UTF-8

import unittest

from typing import List
import sys

class Solution:
    # Time complexity : O(n)
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)): 
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

class TestSolution(unittest.TestCase):
    def testRemoveElement(self):
        s = Solution()
        self.assertEqual(2, s.removeElement([3,2,2,3], 3))
        self.assertEqual(5, s.removeElement([0,1,2,2,3,0,4,2], 2))

def main():
    unittest.main()

if __name__ == "__main__":
    main()