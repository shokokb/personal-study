class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        d = { "1" : "1", "2" : "", "3" : "", "4" : "", "5" : "", 
              "6" : "9", "7" : "", "8" : "8", "9" : "6", "0" : "0"}
        return ("".join(list(map(lambda x : d[x], num[::-1])))) == num