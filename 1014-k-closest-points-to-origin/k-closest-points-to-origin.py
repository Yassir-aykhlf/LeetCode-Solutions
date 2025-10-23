class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # return heapq.nsmallest(k, points, key=lambda x: x[0]*x[0] + x[1]*x[1])
        return [point for point in sorted(points, key=lambda x: x[0]*x[0] + x[1]*x[1])[:k]]