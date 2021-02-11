class Solution:
    def __init__ (self):
        self.steps = dict()
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        ret = 0
        try:
            ret += self.steps[n-2]
        except:
            self.steps[n-2] = self.climbStairs(n - 2)
            ret += self.steps[n-2]
        try:
            ret += self.steps[n-1]
        except:
            self.steps[n-1] = self.climbStairs(n - 1)
            ret += self.steps[n-1]
        return ret