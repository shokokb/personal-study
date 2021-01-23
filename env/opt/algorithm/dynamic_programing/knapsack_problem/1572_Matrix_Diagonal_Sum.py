class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        mat_length = len(mat)
        ret = 0
        x, y = 0, 0
        for i in range(mat_length):
            ret += mat[x][y]
            x += 1
            y += 1
        x, y = mat_length - 1, 0
        for i in range(mat_length):
            ret += mat[x][y]
            x -= 1
            y += 1
        if mat_length % 2 == 1:
            ret -= mat[mat_length // 2][mat_length // 2]
        return ret
        
        