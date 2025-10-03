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
        # O(1)
        return \
            n > 0 and \
            (n & (n - 1) == 0) and \
            (n - 1) % 3 == 0
            # 2^x power of two
            # 1   → 0b0001
            # 2   → 0b0010
            # 4   → 0b0100
            # 8   → 0b1000
            # 4^x
            # 4^0 = 1 → 1 - 1 = 0 → 0 % 3 = 0
            # 4^1 = 4 → 4 - 1 = 3 → 3 % 3 = 0
            # 4^2 = 16 → 16 - 1 = 15 → 15 % 3 = 0
            # 4^3 = 64 → 64 - 1 = 63 → 63 % 3 = 0

class TestSolution(unittest.TestCase):
    def testIsPowerOfFour(self):
        s = Solution()
        self.assertEqual(True,   s.isPowerOfFour(1))
        self.assertEqual(False,  s.isPowerOfFour(2))
        self.assertEqual(False,  s.isPowerOfFour(3))
        self.assertEqual(True,   s.isPowerOfFour(4))
        self.assertEqual(False,  s.isPowerOfFour(5))
        self.assertEqual(False,  s.isPowerOfFour(6))
        self.assertEqual(False,  s.isPowerOfFour(7))
        self.assertEqual(False,  s.isPowerOfFour(8))
        self.assertEqual(False,  s.isPowerOfFour(9))
        self.assertEqual(False,  s.isPowerOfFour(10))
        self.assertEqual(True,   s.isPowerOfFour(16))

def main():
    unittest.main()

if __name__ == "__main__":
    main()

