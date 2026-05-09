class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda pt: pt[0]*pt[0] + pt[1]*pt[1])[:k]