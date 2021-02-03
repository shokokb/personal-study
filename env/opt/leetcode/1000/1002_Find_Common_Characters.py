class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        ans = ""
        n = len(A)
        cnt = [collections.Counter(s) for s in A]
        for c in cnt[0].keys():
            count = min([cnt[i][c] for i in range(n)])
            if count > 0:
                ans += c * count
        return list(ans)
        