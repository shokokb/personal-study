class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # intervals.sort()
        # print(intervals)
        is_necessary = [True for _ in range(len(intervals))]
        for i in range(len(intervals)):
            for j in range(0,i):
                if not is_necessary:
                    break
                if intervals[j][0] <= intervals[i][0] and \
                   intervals[i][1] <= intervals[j][1]:
                    is_necessary[i] = False
                if intervals[i][0] <= intervals[j][0] and \
                   intervals[j][1] <= intervals[i][1]:
                    is_necessary[j] = False
        return is_necessary.count(True)
        