class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        d = x ^ y
        return bin(d)[2:].count("1")
        