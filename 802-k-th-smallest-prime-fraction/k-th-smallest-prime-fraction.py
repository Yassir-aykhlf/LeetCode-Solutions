class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        min_heap = []
        n = len(arr)
        for j in range(1, n):
            heapq.heappush(min_heap, (arr[0] / arr[j], 0, j))
        for _ in range(k - 1):
            frac, i, j = heapq.heappop(min_heap)
            if i + 1 < j:
                heapq.heappush(min_heap, (arr[i + 1] / arr[j], i + 1, j))
        _, i, j = min_heap[0]
        return [arr[i], arr[j]]