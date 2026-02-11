class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals += [newInterval]
        intervals.sort()
        result = [intervals[0]]
        for inter in intervals[1:]:
            last_inter = result[-1]
            if inter[0] <= last_inter[1]:
                last_inter[1] = max(last_inter[1], inter[1])
            else:
                result.append(inter)
        return result