class Solution:
    def mySqrt(self, x: int) -> int:
        n = x // 2
        while True:
            if n ** 2 <= x and (n + 1) ** 2 > x: 
                return n
            if n ** 2 < x:
                n += 1
            if n ** 2 > x:
                n //= 2 