# 7. Reverse Integer

import unittest

# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
class Solution:
    def reverse(self, x: int, plan:int = 0) -> int:
        ret = 0

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if plan == 1:
            # 1.Convert the value to a string, and then revert it 
            # str() で文字列にして、[::-1] で反転
            text = str(x)[::-1]
            
            # Put a sign at the top
            if text[-1] == "-":
                text = "-" + text[:-1]
            ret = int(text)

            # Check the range of the return value
            if ret < INT_MIN or INT_MAX < ret:
                ret = 0

            return ret
        else :
            # 2. Reverse the number mathmatically (decimal surplus and division)
            ret = 0
            sign = -1 if x < 0 else 1
            absolute_x = x * sign 

            while absolute_x > 0:
                ret = ret * 10 + absolute_x % 10
                absolute_x = absolute_x // 10
            ret = sign *  ret

            # Check the range of the return value
            if ret < INT_MIN or INT_MAX < ret:
                ret = 0

            return ret 
            
class TestSolution(unittest.TestCase):
    def testReverse(self):
        s = Solution()
        self.assertEqual(321, s.reverse(123))
        self.assertEqual(-321, s.reverse(-123))
        self.assertEqual(21, s.reverse(120))

def main():
    unittest.main()

if __name__ == "__main__":
    main()
        