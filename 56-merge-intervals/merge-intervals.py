class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]
        for inter in intervals[1:]:
            if inter[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], inter[1])
                last_end = inter[1]
            else:
                result.append(inter)
        return result