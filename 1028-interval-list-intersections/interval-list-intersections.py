class Solution:
    def intervalIntersection(self, l1: List[List[int]], l2: List[List[int]]) -> List[List[int]]:
        p1, p2 = 0, 0
        res = []
        while p1 < len(l1) and p2 < len(l2):
            s1, e1 = l1[p1]
            s2, e2 = l2[p2]
            inter_s = max(s1, s2)
            inter_e = min(e1, e2)
            if inter_s <= inter_e:
                res.append([inter_s, inter_e])
            if e1 < e2:
                p1 += 1
            else:
                p2 += 1
        return res