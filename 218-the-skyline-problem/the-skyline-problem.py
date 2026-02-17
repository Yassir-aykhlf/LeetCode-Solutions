class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for left, right, height in buildings:
            events.append((left, -height))
            events.append((right, height))
        events.sort()

        result = []
        heap = [0]
        prev_max_height = 0

        for x, h in events:
            if h < 0:
                heapq.heappush(heap, h)
            else:
                heap.remove(-h)
                heapq.heapify(heap)

            curr_max_height = -heap[0]
            
            if curr_max_height != prev_max_height:
                result.append([x, curr_max_height])
                prev_max_height = curr_max_height

        return result