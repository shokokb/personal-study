class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            s = 0
            while n > 0:
                s += (n % 10) ** 2
                n //= 10
            if s in seen:
                return False
            print(s)
            seen.add(s)
            if s == 1:
                return True
            n = s