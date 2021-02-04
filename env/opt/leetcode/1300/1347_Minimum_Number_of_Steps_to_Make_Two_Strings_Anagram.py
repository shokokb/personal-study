class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt_s = collections.Counter(s)
        cnt_t = collections.Counter(t)
        chrs = set(list(s + t))
        ret = 0
        for c in chrs:
            ret += abs(cnt_s[c] - cnt_t[c])
        return ret // 2
        