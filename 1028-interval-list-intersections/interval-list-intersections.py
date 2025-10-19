class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        p1, p2 = 0, 0
        result = []
        while p1 < len(firstList) and p2 < len(secondList):
            s1, e1 = firstList[p1]
            s2, e2 = secondList[p2]
            inter_start = max(s1, s2)
            inter_end = min(e1, e2)
            if inter_start <= inter_end:
                result.append([inter_start, inter_end])
            if e1 < e2:
                p1 += 1
            else:
                p2 += 1
        return result