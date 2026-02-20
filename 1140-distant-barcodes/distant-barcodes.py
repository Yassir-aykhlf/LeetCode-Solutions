class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        freq = Counter(barcodes)
        max_heap = [(-count, num) for num, count in freq.items()]
        heapq.heapify(max_heap)
        res = []
        prev_count, prev_val = 0, 0
        while max_heap:
            count, val = heapq.heappop(max_heap)
            res.append(val)
            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_val))
            prev_count, prev_val = count + 1, val
        return res