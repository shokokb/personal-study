class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        q = deque(piles)        
        mine = 0
        while q:
            q.pop()
            mine += q.pop()
            q.popleft()
        return mine   