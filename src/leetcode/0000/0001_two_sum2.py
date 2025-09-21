import unittest
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time Complexity = O(n)
        # Spece Complexity = 0(n)
        d = {}
        for i, v in enumerate(nums):
            if target - v in d:
                return [d[target - v], i] #O(1)
            else:
                d[v] = i 
        return []

class TestSolution(unittest.TestCase):
    def testTwoSum(self):
        s = Solution()
        self.assertEqual([0,1],s.twoSum([2,7,11,15],9)) 
        self.assertEqual([1,2],s.twoSum([3,2,4],6)) 
        self.assertEqual([0,1],s.twoSum([3,3],6)) 

def main():
    unittest.main()

if __name__ == "__main__":
    main()