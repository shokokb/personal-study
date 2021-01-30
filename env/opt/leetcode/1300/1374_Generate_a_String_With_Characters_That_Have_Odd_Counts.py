class Solution:
    def generateTheString(self, n: int) -> str:
        if n == 1:
            return "a"
        if n == 2:
            return "ab"
        if n % 2 == 0:
            return "a" + "b" * (n - 1)
        else:
            return "a" + "b" + "c" * (n - 2) 
        