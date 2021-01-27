class Solution:
    def getRow(self, rowIndex: int) -> List[int]: 

        def getNum(row:int, col:int) -> int:
            if row == 0 or col == 0 or row == col:
                return 1
            return getNum(row-1, col-1) + getNum(row-1, col) 

        
        ans = []
        for col in range(rowIndex + 1):
            ans.append(getNum(rowIndex, col))
        return ans

        
        