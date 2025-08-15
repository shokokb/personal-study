# coding : UTF-8

import unittest

class MergeSort:
    @staticmethod
    def sort():
        return []

class TestMergeSort(unittest.TestCase):

    def test_sort(self):
        self.assertEqual([1, 2, 3, 4, 6], MergeSort.sort([1, 3, 2, 6, 4]))

def main():
    unittest.main()

if __name__ == "__main__":
    main()