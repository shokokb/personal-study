class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i > 0 and j > 0:
                    if  matrix[i][j] == 1:
                        matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])  + 1 
        return (sum(sum(m) for m in matrix))
                