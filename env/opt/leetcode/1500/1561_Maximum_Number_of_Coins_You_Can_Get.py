class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        mine = 0
        while piles:
            piles.pop()
            mine += piles.pop()
            piles.pop(0)
        return mine   