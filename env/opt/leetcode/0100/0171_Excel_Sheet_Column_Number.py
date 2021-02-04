class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        l = list(s)
        while l:
            a = l.pop(0)
            ans *= 26
            ans += ord(a) - ord('A') + 1
        return ans
        