class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return heapq.nsmallest(k, points, key=lambda x: x[0] * x[0] + x[1] * x[1])
        # def dist(idx):
        #     return points[idx][0] ** 2 + points[idx][1] ** 2
        # l, r = 0, len(points) - 1
        # while l <= r:
        #     pivot_idx = randint(l, r)
        #     points[pivot_idx], points[r] = points[r], points[pivot_idx]
        #     pivot = dist(r)
        #     cursor = l
        #     for i in range(l, r):
        #         if dist(i) < pivot:
        #             points[cursor], points[i] = points[i], points[cursor]
        #             cursor += 1
        #     points[cursor], points[r] = points[r], points[cursor]
        #     if cursor == k:
        #         return points[:k]
        #     elif cursor < k:
        #         l = cursor + 1
        #     else:
        #         r = cursor - 1
        # return points