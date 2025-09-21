class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        v = []
        for row in range(rowIndex + 1):
            v.append([0] * (row + 1))
        # print(v)

        for row in range(rowIndex + 1):
            for col in range(row + 1):
                if row == 0 or col == 0 or col == row:
                    v[row][col] = 1
                    continue
                v[row][col] = v[row-1][col-1] + v[row-1][col]

        return v[rowIndex]
