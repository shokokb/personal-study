class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ret = []
        s += " "
        prev = ""
        cnt = 0
        prev_i = 0
        for i, c in enumerate(s) :
            if prev == c:
                cnt += 1
            else:
                if prev != "" and cnt >= 3:
                    ret.append([prev_i, prev_i + cnt - 1])
                cnt = 1
                prev_i = i
            prev = c 
        return ret
            
