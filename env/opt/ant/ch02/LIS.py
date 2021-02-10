n = 5
a = [4,2,3,1,5]
dp = [1 for _ in range(n)]
for i in range(n):
    for j in range(0, i):
        if a[j] < a[i]:
            dp[i] = max([dp[i], dp[j] + 1]) 
print(dp) 
print(dp[n-1])  