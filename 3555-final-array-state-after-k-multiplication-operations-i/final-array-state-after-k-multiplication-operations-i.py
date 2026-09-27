class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        res = nums[::]
        heap = [(n, i) for i, n in enumerate(nums)]
        heapq.heapify(heap)
        for i in range(k):
            n, i = heapq.heappop(heap)
            res[i] *= multiplier
            heapq.heappush(heap, (res[i], i))
        return res