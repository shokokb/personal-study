class Solution:
    def sumZero(self, n: int) -> List[int]:
        ret = []
        if n % 2 == 1:
            ret.append(0)
        for i in range(1, n // 2 + 1):
            ret.extend([i, -i])
        return ret