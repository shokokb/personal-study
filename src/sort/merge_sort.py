# coding : UTF-8

import unittest

# Time complexity: O(nlog(n))
class MergeSort:
    @staticmethod
    def sort(l):
        if len(l) <= 1:
            return l

        mid = len(l) // 2
        left_arr = l[:mid]
        right_arr = l[mid:]

        sorted_left = MergeSort.sort(left_arr)      # O(log(n)
        sorted_right = MergeSort.sort(right_arr)
        # print(left_arr, right_arr, sorted_left, sorted_right)

        res = []
        i, j = 0, 0
        while i < len(sorted_left) and j < len(sorted_right):   # O(n)
            if sorted_left[i] < sorted_right[j]:
                res.append(sorted_left[i])
                i += 1
            else:
                res.append(sorted_right[j])
                j += 1
        if i < len(sorted_left):
            res += sorted_left[i:]
        if j < len(sorted_right):
            res += sorted_right[j:]   
        # while sorted_left and sorted_right:         # O(n)
        #     res.append(sorted_left.pop(0) if sorted_left[0] < sorted_right[0] else sorted_right.pop(0)) # pop(0)=O(n)
        # res += sorted_left if sorted_left else sorted_right

        return res

class TestMergeSort(unittest.TestCase):
    def test_sort(self):
        self.assertEqual([1, 2, 3, 4, 6], MergeSort.sort([1, 3, 2, 6, 4]))

def main():
    unittest.main()

if __name__ == "__main__":
    main()