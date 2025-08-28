# === Imports ===
import math
import unittest
import sys
import time

sys.setrecursionlimit(1500)

# === Recursive Implementation (Original) ===
# Time complexity = O(n)
# Space complexity = O(n)  # due to recursion call stack

# def factorial_recursive(n):
#     """
#     Calculate factorial recursively.
#
#     Args:
#         n (int): Non-negative integer.
#
#     Returns:
#         int: Factorial of n.
#
#     Raises:
#         ValueError: If n is negative.
#         RecursionError: If n > 1000.
#     """
#     if n == 0:
#         return 1
#     if n < 0:
#         raise ValueError("n must be a non-negative integer")
#     if n > 1000:
#         raise RecursionError("n must be an integer less than or equal to 1000")
#     return n * factorial_recursive(n - 1)

# === Iterative Implementation (Current) ===
# Time complexity = O(n)
# Space complexity = O(1)

# d = {0 : 1}

def factorial(n, recursive = True):
    """
    Calculate factorial iteratively.

    Args:
        n (int): Non-negative integer.

    Returns:
        int: Factorial of n.

    Raises:
        ValueError: If n is negative.
    """

    # global d
    
    # if n in d:
    #     return d[n] # O(1) memo

    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    if n == 0: # Base case
        return 1
        # return d[n]

    result = 1
    # Iteratively multiply from 1 to n to calculate factorial
    if recursive:
        result = n * factorial(n - 1) # Recursive
    else :
        for number in range(1, n + 1): # O(n)
            result *= number
    return result

# === Unit Tests ===
class TestFactorial(unittest.TestCase):
    def test_factorial_positive(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(1000), math.factorial(1000))

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError) as context:
            factorial(-1)
        self.assertEqual(str(context.exception), "n must be a non-negative integer")

def main():
    # === Main Execution (Example Usage) ===
    try:
        print(factorial(5))  # Expect 120
    except ValueError as e:
        print(f"Error: {e}")

    start_time = time.time()
    answer = factorial(1000, recursive = False)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time with loop: {elapsed_time}")

    start_time = time.time()
    answer = factorial(1000, recursive = True)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time with recursion: {elapsed_time}")
    

if __name__ == "__main__":
    main()
    unittest.main()
