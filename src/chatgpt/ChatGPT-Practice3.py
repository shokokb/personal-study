# coding: UTF-8

import unittest

def factorial(n):
    if n == 0:
        return 1
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    return n * factorial(n - 1) # n!

try:
    print(factorial(5)) # Expect 120
except ValueError as e:
    print(f"Error: {e}")

class TestFactorial(unittest.TestCase):
    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(3), 6)

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError) as context:
            factorial(-1)
        self.assertEqual(str(context.exception), "n must be a non-negative integer")

if __name__ == "__main__":
    unittest.main()