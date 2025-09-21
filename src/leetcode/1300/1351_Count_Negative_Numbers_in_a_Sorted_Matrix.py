class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cnt = 0
        for nums in grid:
            cnt += len(list(filter(lambda x: x < 0, nums)))
        return cnt
        