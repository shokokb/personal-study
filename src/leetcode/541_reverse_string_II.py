# coding : UTF-8

import unittest

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        start = 0
        n = len(s)
        ret = []
        while start <= n:
            # print(s[start:start+2*k])
            ret.append(s[start:start+k][::-1])
            ret.append(s[start+k:start+2*k])
            start += 2*k
        return "".join(ret)
        

class TestSolution(unittest.TestCase):
    def testReverseStr(self):
        s = Solution()
        self.assertEqual("bacdfeg",s.reverseStr("abcdefg",2))
        self.assertEqual("bacd",s.reverseStr("abcd",2))

def main():
    unittest.main()

if __name__ == "__main__":
    main()

