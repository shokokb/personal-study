class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ret = arr
        for i, n in enumerate(arr):
            ret[i] = max(arr[i+1:]) if i != len(arr) - 1 else -1
        return ret
            
        