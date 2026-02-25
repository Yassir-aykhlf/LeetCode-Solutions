class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        freq = Counter(barcodes)
        max_heap = [(-count, code) for code, count in freq.items()]
        heapq.heapify(max_heap)
        prev = None
        res = []
        while max_heap:
            count, code = heapq.heappop(max_heap)
            res.append(code)
            count += 1
            if prev and prev[0] < 0:
                heapq.heappush(max_heap, prev)
            prev = (count, code)
        return res