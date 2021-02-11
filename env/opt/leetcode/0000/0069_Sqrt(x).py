class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        left = 2
        right = x // 2
        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot ** 2
            if num > x:
                right = pivot - 1
            elif num < x:
                left = pivot + 1
            else:
                return pivot
        return right