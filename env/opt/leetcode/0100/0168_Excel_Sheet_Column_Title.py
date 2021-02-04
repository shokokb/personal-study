class Solution:
    def convertToTitle(self, n: int) -> str:
        result = ""
        while n > 0:
            n -= 1
            n, m = divmod(n, 26)
            result += chr(65 + m)
        return result[::-1]  