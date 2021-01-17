class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arr = []
        for i in range(n):
            sumv = nums[i]
            arr.append(sumv)
            for j in range(i+1, n):
                sumv += nums[j]
                arr.append(sumv)
        # print(arr)
        arr.sort()
        return sum(arr[left-1:right]) % (10**9 + 7)
        