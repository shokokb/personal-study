# coding : UTF-8

import unittest

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(" : ")", "[" : "]", "{" : "}"}
        stack = list()
        for x in s:
            if x in ["(", "{", "["]:
                stack.append(x)
            else:
                if stack:
                    if pairs[stack.pop()] != x:
                        return False
                else:
                    return False
        return not stack

class TestSolution(unittest.TestCase):
    def testIsValud(self):
        s = Solution()
        self.assertEqual(True, s.isValid("()"))
        self.assertEqual(True, s.isValid("()[]{}"))
        self.assertEqual(False, s.isValid("(]"))
        self.assertEqual(True, s.isValid("([])"))
        self.assertEqual(False, s.isValid("([)]")) 

def main():
    unittest.main()

if __name__ == "__main__":
    main()