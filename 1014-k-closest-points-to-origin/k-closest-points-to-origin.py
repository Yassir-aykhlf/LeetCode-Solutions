class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        point_gen = (((x*x + y*y), ([x, y])) for x, y in points)
        point_list = list(point_gen)
        point_list.sort()
        k_points = itertools.islice(point_list, k)
        return [point for _, point in sorted(k_points)]