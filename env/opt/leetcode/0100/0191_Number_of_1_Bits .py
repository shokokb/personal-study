class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = 0
        while n > 0: #nは2以上
            if n % 2 == 1: ret += 1
            n = n // 2
        return ret
        