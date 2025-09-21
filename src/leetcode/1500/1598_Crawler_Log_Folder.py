class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for log in logs:
            if log == "../":
                ans -= 1 if ans > 0 else 0
            elif log != "./":
                ans += 1
        return ans