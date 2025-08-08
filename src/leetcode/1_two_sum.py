import unittest
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # 1. Naive idea(O(n^2))
        # for idx1 in range(len(nums)):
        #     for idx2 in range(idx1 + 1, len(nums)):
        #         if nums[idx1] + nums[idx2] == target:
        #             return [idx1, idx2]
        # return []

        # Better idea
        # Using a hashtable
        my_dict = {}
        for i, num in enumerate(nums):
            try:
                if (my_dict[target - num] is not None):
                    return [my_dict[target - num], i]             
            except KeyError:
                my_dict[num] = i
        return []

        # Another idea(???)
        # Sort nums at first, and find the other number by using binary search

class TestSolution(unittest.TestCase):
    def testTwoSum(self):
        sl = Solution()

        # Example 1:
        # Input: nums = [2, 7, 11, 15], target = 9
        # Output: [0,1]
        # Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
        self.assertEqual([0, 1], sl.twoSum([2, 7, 11, 15], 9))

        # Example 2:
        # Input: nums = [3, 2, 4], target = 6
        # Output: [1, 2]
        self.assertEqual([1, 2], sl.twoSum([3, 2, 4], 6))

        # Example 3:
        # Input: nums = [3, 3], target = 6
        # Output: [0, 1]
        self.assertEqual([0, 1], sl.twoSum([3, 3], 6))

        
        # Example 4:
        # Input: nums = [2,7,11,15], target = 8
        # Output: []
        # Explanation: Because nums[idx1] + nums[idx2] != 8, we return [].
        self.assertEqual([], sl.twoSum([2, 7, 11, 15], 8))

if __name__ == "__main__":
    unittest.main()

#---
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?