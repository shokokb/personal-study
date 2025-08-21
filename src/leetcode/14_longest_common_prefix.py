# coding;UTF-8

import unittest
from typing import List 

class Solution:
    def partLongestCommonPrefix(self, strs: List[str], s:int, t:int) -> str:
        if not strs:
            return ""

        if t <= s:
            return ""

        pivot = (s+t+1) // 2


        
        return ""

    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 1. Easiest Way (Linear Search)
        # if not strs:
        #     return ""
        # min_len = min(len(s) for s in strs)
        # for i in range(min_len):    # O(m)
        #     if any(s[i] != strs[0][i] for s in strs):
        #     # char_set = set(s[i] for s in strs) #(O)
        #     # if len(char_set) != 1:
        #         return strs[0][:i]
        # return strs[0][:min_len] 
        
        # 2. Dictionary Sort
        # O(nlogn)
        # if not strs:
        #     return ""
        # strs.sort() # O(nlogn)
        # min_len = min(len(strs[0]), len(strs[-1]))
        # for i in range(min_len): # m
        #     if strs[0][i] != strs[-1][i]:
        #         return strs[0][:i]
        # return strs[0][:min_len]

        # 3. Using Pivot
        if not strs:
            return ""

        prefix = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < len(strs[i]) and j < len(prefix) and prefix[j] == strs[i][j]:
                j += 1
            prefix = prefix[:j]  
        if prefix == "":
            return prefix          
        return prefix

class TestSolution(unittest.TestCase):
    def testLongestCommonPrefix(self):
        s = Solution()
        self.assertEqual("fl", s.longestCommonPrefix(["flower","flow","flight"]))
        self.assertEqual("", s.longestCommonPrefix(["dog","racecar","car"]))
        self.assertEqual("", s.longestCommonPrefix([]))


def main():
    unittest.main()

if __name__ == "__main__":
    main()