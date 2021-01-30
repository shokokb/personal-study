class Solution:
    def minOperations(self, n: int) -> int:
        arr = [2 * i + 1 for i in range(n)]
        # print(arr)
        center = (arr[0] + arr[-1]) // 2
        # print("center", center)
        pivot = (n - 1) // 2
        # print("pivot", pivot)
        cnt = 0
        if n % 2 == 0:
            for i in range(pivot + 1):
                cnt += center - arr[i]
        else:
            for i in range(pivot + 1):
                cnt += center - arr[i]
        return cnt