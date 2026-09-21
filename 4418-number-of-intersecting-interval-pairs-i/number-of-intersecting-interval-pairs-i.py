class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        count = 0
        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                if intervals[j][0] <= intervals[i][1]:
                    count += 1
        return count