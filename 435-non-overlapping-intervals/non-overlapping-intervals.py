class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort the intervals by end so each interval have the interval ending before it, behind it
        # and
        # by sorting by the ending, we automatically only remove if necessary
        # minimizing the number of removals
        intervals.sort(key=lambda i: i[1])
        removals = 0
        # loop through the intervals and detect overlaps
        last_end = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] < last_end:
                removals += 1
            else:
                last_end = interval[1]
        return removals