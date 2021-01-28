class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ret = []
        for i in range(len(arr) - 1, -1, -1):
            if i == len(arr) - 1:
                ret.insert(0, -1)
                continue
            ret.insert(0, max(arr[i+1], ret[0]))
        return ret