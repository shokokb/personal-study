class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        mat_length = len(mat)
        ret = 0
        x1, x2, y = 0, mat_length - 1, 0
        for i in range(mat_length):
            ret += mat[x1][y] + mat[x2][y]
            x1 += 1
            x2 -= 1
            y += 1
        if mat_length % 2 == 1:
            ret -= mat[mat_length // 2][mat_length // 2]
        return ret