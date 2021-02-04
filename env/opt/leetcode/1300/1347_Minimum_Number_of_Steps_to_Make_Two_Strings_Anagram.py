class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d = defaultdict(lambda:0)
        for c in s:
            d[c] += 1
        for c in t:
            d[c] -= 1
        return sum([v for v in d.values() if v > 0])
            
        