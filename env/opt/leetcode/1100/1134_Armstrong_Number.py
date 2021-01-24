class Solution:
    def isArmstrong(self, N: int) -> bool:
        digit = len(list(str(N)))
        sumv = 0
        n = N
        while n > 0:
            sumv += (n % 10) ** digit
            n //= 10
        return N == sumv