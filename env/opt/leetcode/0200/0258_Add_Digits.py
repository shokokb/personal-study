class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            s = 0
            while num > 0:
                s += num % 10
                num //= 10
            if s < 10:
                return s
            else:
                num = s