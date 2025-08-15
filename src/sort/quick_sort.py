# coding : UTF-8

import sys
import unittest

sys.setrecursionlimit(1500)

class QuickSort:

    # Time Complexity : O(nlogn), but O(n^2) in the worst case
    # Space Complexity: O(1)
    def sort (l) :

        """
        Quick sort

        Args:
            l (list): number list

        Returns:
            l: sorted list
        """        
        if len(l) < 2:
            return l
        
        # Partitioning
        pivot = l[-1]
        left =  [v for v in l[:-1] if v <= pivot]
        right = [v for v in l[:-1] if v >  pivot]
        # Divide and Conquer
        # Combine
        return QuickSort.sort(left) + [pivot] + QuickSort.sort(right) # O(log(n))

# === Unit Tests ===
class TestQuickSort(unittest.TestCase):
    def test_sort(self):
        self.assertEqual(QuickSort.sort([3, 2, 4, 5 , 1, 3]), [1, 2, 3, 3, 4, 5])
        self.assertEqual(QuickSort.sort([]), [])

def main():
    unittest.main()
    # target = [3, 2, 4, 5 , 1, 3]
    # sorted_target = QuickSort.sort(target)
    # print(sorted_target)

if __name__ == "__main__":
    main()