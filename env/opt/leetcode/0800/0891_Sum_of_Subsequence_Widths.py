class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        ret = 0
        A.sort()
        n = len(A)
        for i in range(n):
            ret += (2**i - 2 **(n - i - 1)) * A[i]
        return ret % (10**9 + 7)