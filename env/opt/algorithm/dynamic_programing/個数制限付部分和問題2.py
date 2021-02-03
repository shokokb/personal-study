# coding: UTF-8
from typing import List

def answer(n:int, a:List[int], m:List[int], k:int):
    dp = [[False for _ in range(k + 1)] for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(K + 1):
            for k in range(m[i] + 1):
                if k * a[i] > j:
                    break
                dp[i + 1][j] |= dp[i][j - k * a[i]]
    return dp[n][K]

if __name__ == "__main__":
    n = 3
    a = [3, 5, 8]
    m = [3, 2, 2]
    K = 17
    print(answer(n, a, m, K))
