from typing import List

import unittest

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        # # Time Complexity: O(n^2)
        # # Spece Complexity:O(1)
        # for l in range(n):
        #     for r in range(l+1,n):
        #        res = max(res, (r-l)*min(height[l],height[r]))
        # # Time Complexity: O(n)
        # # Spece Complexity:O(1)
        l = 0
        r = n-1
        while l < r:
            res = max(res, (r-l)*min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res

class TestSolution(unittest.TestCase):
    def testMaxArea(self):
        s = Solution()
        self.assertEqual(49, s.maxArea([1,8,6,2,5,4,8,3,7]))


def main():
    unittest.main()

if __name__ == "__main__":
    main()