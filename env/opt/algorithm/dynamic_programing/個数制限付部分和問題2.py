# coding: UTF-8
from typing import List

def answer(n:int, a:List[int], m:List[int], k:int):
    dp = [-1 for _ in range(k + 1)]
    dp[0] = 0
    for i in range(n):
        for j in range(K + 1):
            if dp[j] >= 0:
                dp[j] = m[i]
            elif j < a[i] or dp[j - a[i]] <= 0:
                dp[j] = -1
            else:
                dp[j] = dp[j - a[i]] - 1
    return dp[K] >= 0

if __name__ == "__main__":
    n = 3
    a = [3, 5, 8]
    m = [3, 2, 2]
    K = 17
    print(answer(n, a, m, K))
