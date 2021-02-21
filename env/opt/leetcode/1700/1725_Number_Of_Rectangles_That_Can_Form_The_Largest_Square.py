class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        squares = []
        max_len = 0
        for l, w in rectangles:
            length = min(l, w)
            max_len = max(max_len, length)
            squares.append(length)
        return (len(list(filter(lambda x: x == max_len, squares))))
        