class Solution:
    def binary_search(self, matrix:List[List[int]], \
                      target:int, start:int, vertical:bool) -> bool:
        low = start
        high = len(matrix[0]) - 1 if vertical else len(matrix) - 1
        while low <= high:
            mid = (low + high) // 2
            if vertical:
                if matrix[start][mid] < target:
                    low = mid + 1
                elif matrix[start][mid] > target:
                    high = mid - 1
                else:
                    return True
            else:
                if matrix[mid][start] < target:
                    low = mid + 1
                elif matrix[mid][start] > target:
                    high = mid - 1
                else:
                    return True
        return False
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(min(len(matrix), len(matrix[0]))):
            v = self.binary_search(matrix, target, i, True)
            h = self.binary_search(matrix, target, i, False)
            if v or h:
                return True
        return False