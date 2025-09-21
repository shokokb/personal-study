class Solution:
    def __init__ (self):
        self.results = dict()
        
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        ret = 0
        try:
            ret += self.results[n-3]
        except KeyError:
            self.results[n-3] = self.tribonacci(n-3) 
            ret += self.results[n-3]            
        try:
            ret += self.results[n-2]
        except KeyError:
            self.results[n-2] = self.tribonacci(n-2) 
            ret += self.results[n-2]
        try:
            ret += self.results[n-1]
        except KeyError:
            self.results[n-1] = self.tribonacci(n-1) 
            ret += self.results[n-1]
        return ret
        