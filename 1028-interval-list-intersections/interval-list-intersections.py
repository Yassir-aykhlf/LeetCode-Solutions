class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        l1, l2 = firstList, secondList
        res = []
        p1, p2 = 0, 0
        while p1 < len(l1) and p2 < len(l2):
            s1, e1 = l1[p1]
            s2, e2 = l2[p2]
            inter_left, inter_right = max(s1, s2), min(e1, e2)
            if inter_left <= inter_right:
                res.append([inter_left, inter_right])
            if e1 < e2:
                p1 += 1
            else:
                p2 += 1
        return res