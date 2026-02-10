"""
Given an array of intervals where intervals[i] = [starti, endi]
merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        result = [intervals[0]]
        for current in intervals[1:]:
            last_inter = result[-1]
            if current[0] <= last_inter[1]:
                last_inter[1] = max(current[1], last_inter[1])
            else:
                result.append(current)
        return result