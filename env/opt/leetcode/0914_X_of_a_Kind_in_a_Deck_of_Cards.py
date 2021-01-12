class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        c = collections.Counter(deck)
        cnt = sorted(list(set(c.values())))
        
        if len(cnt) == 0: return False
        
        if cnt[0] == 1: return False
        
        for m in range(2, cnt[0] + 1):
            if all([x % m == 0 for x in cnt]):
                return True
            
        return False