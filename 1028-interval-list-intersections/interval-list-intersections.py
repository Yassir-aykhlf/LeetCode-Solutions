class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        l1, l2 = firstList, secondList
        if not l1 or not l2:
            return []
        p1, p2 = 0, 0
        result = []
        while p1 < len(l1) and p2 < len(l2):
            s1, e1 = l1[p1]
            s2, e2 = l2[p2]
            inter_start = max(s1, s2)
            inter_end = min(e1, e2)
            if inter_start <= inter_end:
                result.append([inter_start, inter_end])
            if e1 < e2:
                p1 += 1
            else:
                p2 += 1
        return result