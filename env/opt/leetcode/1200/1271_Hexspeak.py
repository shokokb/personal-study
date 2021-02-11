class Solution:
    def toHexspeak(self, num: str) -> str:
        d = {0:"O",1:"I", 0xA:"A", 0xB:"B", 0xC:"C", 0xD:"D", 0xE:"E", 0xF:"F"}
        n = int(num)
        ret = "" 
        try:
            while n:
                ret = d[n % 16] + ret
                n //= 16 
            return ret
        except:
            return "ERROR"
        