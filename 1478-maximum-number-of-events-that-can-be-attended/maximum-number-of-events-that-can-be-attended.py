import heapq

class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        events.sort(key=lambda x: x[0])
        min_heap = []
        attended = 0
        event_idx = 0
        n = len(events)
        day = 0
        while event_idx < n or min_heap:
            if not min_heap:
                day = events[event_idx][0]
            while event_idx < n and events[event_idx][0] <= day:
                heapq.heappush(min_heap, events[event_idx][1])
                event_idx += 1
            heapq.heappop(min_heap)
            attended += 1
            day += 1
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
        return attended