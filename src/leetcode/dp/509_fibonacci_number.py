# coding : UTF-8

import unittest 


class Solution:
    def fib(self, n: int) -> int:
        prev2 = 0
        prev1 = 1

        # Time complexity = O(2^n)->O(n)
        # Space complexity = O(n)->O(1)
        for i in range(2, n+1):
            curr = prev1+prev2
            prev2, prev1 = prev1, curr
        return prev1

class TestSolution(unittest.TestCase):
    def testFib(self):
        s = Solution()
        self.assertEqual(1, s.fib(2))
        self.assertEqual(2, s.fib(3))
        self.assertEqual(3, s.fib(4))
 
def main():
    unittest.main()

if __name__ == "__main__":
    main()