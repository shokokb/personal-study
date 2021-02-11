class Solution:
    def __init__(self):
        self.results = dict()
        
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        ret = 0
        try:
            ret += self.results[n - 1]
        except:
            self.results[n - 1] = self.fib(n - 1)
            ret += self.results[n - 1]
        try:
            ret += self.results[n - 2]
        except:
            self.results[n - 2] = self.fib(n - 2)
            ret += self.results[n - 2]
        return ret