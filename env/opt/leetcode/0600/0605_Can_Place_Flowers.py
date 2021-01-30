class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        for i in range(length):
            if flowerbed[i] == 1:
                if i >= 1:
                    flowerbed[i - 1] = -1 if flowerbed[i - 1] == 0 else flowerbed[i - 1] 
                if i < length - 1:
                    flowerbed[i + 1] = -1 if flowerbed[i + 1] == 0 else flowerbed[i + 1] 
            
        for i in range(n):
            cnt = flowerbed.count(0)
            if cnt < 1:
                return False
            idx = flowerbed.index(0)
            flowerbed[idx] = 1
            if idx >= 1:
                flowerbed[idx - 1] = -1 if flowerbed[idx - 1] == 0 else flowerbed[idx - 1] 
            if idx < length - 1:
                flowerbed[idx + 1] = -1 if flowerbed[idx + 1] == 0 else flowerbed[idx + 1] 
        return True
