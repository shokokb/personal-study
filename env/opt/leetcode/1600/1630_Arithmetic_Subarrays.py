class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ret = []
        for i in range(len(l)):
            arr = nums[l[i]:r[i]+1]
            arr.sort()
            d = arr[1]-arr[0]
            ret.append(all([arr[i+1]-arr[i] == d for i in range(0,len(arr)-1)]))
        return ret