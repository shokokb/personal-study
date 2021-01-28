class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for row_num in range(numRows):
            row = [None for _ in range(row_num + 1)]
            row[0] = row[-1] = 1
            triangle.append(row)
        
        for row in range(numRows):
            l, r = 1, row - 1
            while l <= r:
                triangle[row][l] = \
                triangle[row][r] = \
                triangle[row-1][l-1] + triangle[row-1][l]
                l += 1
                r -= 1
        return triangle