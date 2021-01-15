class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i, price in enumerate(prices):
            price_off = 0
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    price_off = prices[j]
                    break
            prices[i] -= price_off
        return prices