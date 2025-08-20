# coding;UTF-8

import unittest
from typing import List 

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 1. Easiest Way (Linear Search)
        if not strs:
            return ""
        min_len = min(len(s) for s in strs)
        for i in range(min_len):    # O(n)
            if any(s[i] != strs[0][i] for s in strs):
            # char_set = set(s[i] for s in strs) #(O)
            # if len(char_set) != 1:
                return strs[0][:i]
        return strs[0][:min_len]     

class TestSolution(unittest.TestCase):
    def testLongestCommonPrefix(self):
        s = Solution()
        self.assertEqual("fl", s.longestCommonPrefix(["flower","flow","flight"]))
        self.assertEqual("", s.longestCommonPrefix(["dog","racecar","car"]))


def main():
    unittest.main()

if __name__ == "__main__":
    main()