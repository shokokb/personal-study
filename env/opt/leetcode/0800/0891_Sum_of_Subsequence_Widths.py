class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        sumv = 0
        for i in range(2, len(A) + 1):
            items = combinations(A, i)
            for item in items:
                sumv += max(item) - min(item)
        return sumv