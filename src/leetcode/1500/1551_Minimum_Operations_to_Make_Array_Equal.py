class Solution:
    def minOperations(self, n: int) -> int:
        return (n ** 2 - 1) // 4 if n % 2 == 1 else  (n ** 2) // 4