class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        d = x ^ y
        return bin(d).count("1")