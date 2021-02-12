n = 4
m = 3
M = 10000
dp = [[0 for _ in range(n)] for _ in range(m)]

for i in range(m):
    for j in range(n):
        if j >= i:
            dp[i][j] = dp[i-1][j] + dp[i][j-i] % M
        else:
            dp[i][j] = dp[i-1][j]
print(dp)