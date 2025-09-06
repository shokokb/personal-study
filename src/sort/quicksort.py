# coding : UTF-8

import unittest

class Solution:
    @staticmethod
    def quicksort (arr):
        # Base Case
        if len(arr) < 2:
            return arr
        # Piovt
        pivot = arr[-1]
        left  = [v for v in arr[:-1] if v <= pivot]
        right = [v for v in arr[:-1] if v > pivot]
        return Solution.quicksort(left) + [pivot] + Solution.quicksort(right)
 
class TestSolution(unittest.TestCase):
    def testQuicksort(self):
        self.assertEqual([1, 2, 3, 3, 4],Solution.quicksort([2,3,4,1,3]))

def main():
    unittest.main()

if __name__ == "__main__":
    main()