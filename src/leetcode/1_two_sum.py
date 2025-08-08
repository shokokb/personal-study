import unittest

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Basic idea(O(n**2))
        # length = len(nums)
        # for idx1 in range(length):
        #     for idx2 in range(idx1 + 1, length):
        #         if nums[idx1] + nums[idx2] == target:
        #             return [idx1, idx2]

        # Another idea(???)
        # Sort nums at first, and find the other number by using binary search

        # Better idea
        # Using a dictionary as a hashtable
        my_dict = {}
        i = 0
        for num in nums:        # O(n)
            my_dict[num] = i    # O(1)
            i += 1

        i = 0
        for num in nums:
            idx1 = i
            idx2 = my_dict[target - num]
            if idx2 is not None:
                return [idx1, idx2]
        return []

class TestSolution(unittest.TestCase):
    def testTwoSum(self):
        sl = Solution()

        # Example 1:
        # Input: nums = [2,7,11,15], target = 9
        # Output: [0,1]
        # Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
         self.assertEqual([0,1], sl.twoSum([2,7,11,15], 9))

        # Example 2:
        # Input: nums = [3,2,4], target = 6
        # Output: [1,2]
         self.assertEqual([], sl.twoSum([3,2,4], 6))

        # Example 3:
        # Input: nums = [3,3], target = 6
        # Output: [0,1]
         self.assertEqual([0,1], sl.twoSum([3,3]))

if __name__ == "__main__":
    tester = TestSolution()
    tester.testTwoSum()

#---
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?