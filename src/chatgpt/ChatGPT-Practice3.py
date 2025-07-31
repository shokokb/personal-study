# coding: UTF-8

import math
import unittest
import sys

sys.setrecursionlimit(1500)

def factorial(n):
    if n == 0:
        return 1
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n > 1000:
        raise RecursionError("n must be an integer less than or equal to 1000")
    return n * factorial(n - 1) # n!

try:
    print(factorial(5)) # Expect 120
except ValueError as e:
    print(f"Error: {e}")

class TestFactorial(unittest.TestCase):
    def test_factorial_positive(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(1000), math.factorial(1000))
        with self.assertRaises(RecursionError) as context:
            factorial(1001)
        self.assertEqual(str(context.exception), "n must be an integer less than or equal to 1000")

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError) as context:
            factorial(-1)
        self.assertEqual(str(context.exception), "n must be a non-negative integer")

if __name__ == "__main__":
    unittest.main()