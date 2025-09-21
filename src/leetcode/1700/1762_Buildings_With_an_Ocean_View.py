class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans = []
        max_height = 0
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > max_height:
                ans.insert(0, i)
            max_height = max(heights[i], max_height)
        return ans
        