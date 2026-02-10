class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals += [newInterval]
        intervals.sort()
        result = [intervals[0]]
        for current in intervals[1:]:
            last_inter = result[-1]
            if current[0] <= last_inter[1]:
                last_inter[-1] = max(current[1], last_inter[1])
            else:
                result.append(current)
        return result