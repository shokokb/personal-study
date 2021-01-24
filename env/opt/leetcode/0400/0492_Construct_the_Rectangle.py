class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        l = w = math.sqrt(area)
        if w % 1 == 0:
            return [int(l), int(w)]
        W = int(w)
        for w in range(W,0,-1):
            l = area / w
            if l % 1 == 0:
                return [int(l), w]
        