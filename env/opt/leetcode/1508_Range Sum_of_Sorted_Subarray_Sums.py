class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arr = []
        for i in range(n):
            for j in range(i, n):
                arr.append(sum(nums[i:j+1]))
        arr.sort()
        return sum(arr[left-1:right]) % (10**9 + 7)