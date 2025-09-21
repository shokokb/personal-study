class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ret = 0
        strs = list(zip(*strs))
        for s in strs:
            for i in range(1, len(s)):
                if ord(s[i-1]) > ord(s[i]):
                    ret += 1
                    break
        return ret