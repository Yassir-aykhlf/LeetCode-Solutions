class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])
        min_heap = []
        res = [-1] * len(queries)
        i = 0
        n = len(intervals)
        for q, original_idx in sorted_queries:
            while i < n and intervals[i][0] <= q:
                left, right = intervals[i]
                size = right - left + 1
                heapq.heappush(min_heap, (size, right))
                i += 1
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            if min_heap:
                res[original_idx] = min_heap[0][0]
        return res