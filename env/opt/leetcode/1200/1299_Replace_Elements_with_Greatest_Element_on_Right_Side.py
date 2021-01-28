class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = list()
        while arr:
            arr.pop(0)
            ans.append(max(arr) if len(arr) > 0 else -1)        
        return ans
            
        