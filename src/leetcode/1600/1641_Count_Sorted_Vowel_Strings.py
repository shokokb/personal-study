class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[0 for _ in range(5)] for _ in range(0, n + 1)]
        for i in range(5):
            dp[1][i] = 1
        for i in range(2, n + 1):
            dp[i][0] = dp[i-1][0]
            dp[i][1] = dp[i-1][0] + dp[i-1][1]
            dp[i][2] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2]
            dp[i][3] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-1][3]
            dp[i][4] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-1][3] + dp[i-1][4]
        return sum(dp[n])
        