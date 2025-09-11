import unittest
from typing import List 

class Solution:
    def trap(self, height: List[int]) -> int:

        res = 0

        n = len(height)
        left_max = [max(height[:i+1]) for i in range(n)]
        right_max = [max(height[i:]) for i in range(n)]

        for i in range(n):
            res += min(left_max[i], right_max[i]) - height[i]
        return res

class TestSolution(unittest.TestCase):
    def testTrap(self):
        s = Solution()
        self.assertEqual(6, s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))  
        self.assertEqual(9, s.trap([4,2,0,3,2,5]))  

def main():
    unittest.main()

if __name__ == "__main__":
    main()