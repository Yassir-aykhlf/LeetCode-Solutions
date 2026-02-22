class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        arrows = 1
        last_end = points[0][1]
        for point in points[1:]:
            if point[0] > last_end:
                last_end = point[1]
                arrows += 1
        return arrows