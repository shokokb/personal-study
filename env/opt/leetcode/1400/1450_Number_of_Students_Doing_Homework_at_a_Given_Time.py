class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        cnt = 0
        n = len(startTime)
        for i in range(n):
            cnt += 1 if startTime[i] <= queryTime <= endTime[i] else 0
        return cnt
        