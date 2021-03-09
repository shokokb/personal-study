class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ret = math.trunc(dividend / divisor) 
        if ret > 2**31 - 1:
            return 2 ** 31 - 1
        return ret
        