class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d = defaultdict(lambda:0)
        for n in range(lowLimit, highLimit + 1):
            sumv = sum([int(m) for m in list(str(n))])
            d[sumv] += 1
        return max(d.values())