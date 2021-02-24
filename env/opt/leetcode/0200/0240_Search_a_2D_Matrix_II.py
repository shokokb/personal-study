class Solution:
    def binary_search(self, row: List[int], target:int) -> bool:
        if len(row) == 0:
            return False
        mid = len(row) // 2
        if target == row[mid]:
            return True
        elif target < row[mid]:
            return self.binary_search(row[:mid], target)
        else:
            return self.binary_search(row[mid+1:], target)
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if self.binary_search(row, target):
                return True
        return False