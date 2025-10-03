# coding : UTF-8 

import unittest

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 1. Using split
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # words = s.split()
        # if words:
        #     return len(words[-1])
        # else:
        #     return 0
        # 2. back-loop
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        length = 0
        i = len(s) - 1
        while i >= 0 and s[i] == " ":
            i -=1
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1             
        return length


class TestSolution(unittest.TestCase):
    def testLengthOfLastWord(self):
        s = Solution()
        self.assertEqual(5, s.lengthOfLastWord("Hello World"))
        self.assertEqual(4, s.lengthOfLastWord("   fly me   to   the moon  "))
        self.assertEqual(6, s.lengthOfLastWord("luffy is still joyboy"))

def main():
    unittest.main()

if __name__ == "__main__":
    main()