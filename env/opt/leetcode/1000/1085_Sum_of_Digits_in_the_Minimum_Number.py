class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        A.sort()
        a = A[0]
        S = 0 
        while a > 0:
            S += a % 10
            a //= 10
        return 0 if S % 2 == 1 else 1