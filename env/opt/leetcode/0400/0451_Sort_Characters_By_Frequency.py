class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = collections.Counter(s)
        cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
        ret = ""
        for item in cnt:
            ret += item[0] * item[1]
        return ret
        
        