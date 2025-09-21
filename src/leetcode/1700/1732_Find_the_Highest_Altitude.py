class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        height = 0
        highest = 0
        for g in gain:
            height += g
            highest = max(highest, height)
        return highest
        