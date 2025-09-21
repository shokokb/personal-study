class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        ans = []
        low = 0
        high = len(S)
        for c in S:
            if c == 'I':
                ans.append(low)
                low += 1
            else:
                ans.append(high)
                high -= 1
        ans.append(low)
        return ans
        