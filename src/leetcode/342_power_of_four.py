import unittest
import math

# Given an integer n, return true if it is a power of four. Otherwise, return false.
# An integer n is a power of four, if there exists an integer x such that n == 4^x.
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # if n < 0:
        #     return False
        # number = 1
        # while number <= n:
        #     if number == n:
        #         return True
        #     number *= 4
        # return False 

        # ===
        # if n < 0:
        #     return False
        # log_n = math.log(n, 4)
        # return log_n.is_integer()

        #===
        return n > 0 and (n & (n - 1) == 0) and (n - 1) % 3 == 0

class TestSolution(unittest.TestCase):
    def testIsPowerOfFour(self):
        s = Solution()
        self.assertEqual(True,  s.isPowerOfFour(16))
        self.assertEqual(False, s.isPowerOfFour(5))
        self.assertEqual(True,  s.isPowerOfFour(1))

def main():
    unittest.main()

if __name__ == "__main__":
    main()

