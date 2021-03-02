class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        for i in range(len(s) - 1, -1, -1):
            if s[i] * k == s[i:i+k]:
                s = s[:i] + s[i+k:]
        return s

        