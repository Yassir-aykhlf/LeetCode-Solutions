class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        l1, l2 = firstList, secondList
        p1, p2 = 0, 0
        res = []
        while p1 < len(l1) and p2 < len(l2):
            s1, e1 = l1[p1]
            s2, e2 = l2[p2]
            inter_l, inter_r = max(s1, s2), min(e1, e2)
            if inter_l <= inter_r:
                res.append([inter_l, inter_r])
            if e1 < e2:
                p1 += 1
            else:
                p2 += 1
        return res