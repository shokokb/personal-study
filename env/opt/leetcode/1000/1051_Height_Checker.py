class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights_before = heights.copy()
        heights_after  = heights.copy()
        heights_after.sort()
        print(heights_before)
        print(heights_after)
        cnt = 0
        for i, h in enumerate(heights_after):
            if h != heights_before[i]:
                cnt += 1
        return cnt
        