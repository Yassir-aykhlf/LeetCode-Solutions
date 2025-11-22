class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # return sorted(points, key = lambda x: x[0]*x[0] + x[1]*x[1])[:k]
        return heapq.nsmallest(k, points, key = lambda pt: pt[0]**2 + pt[1]**2)