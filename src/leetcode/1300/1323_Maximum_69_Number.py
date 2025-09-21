class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        if s.count('6') > 0:            
            i = s.index('6')
            s = s[0:i] + '9' + s[i+1:]
        return int(s)
        