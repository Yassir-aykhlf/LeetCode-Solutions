class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for count, start, end in trips:
            events.append((start, 1, count))
            events.append((end, 0, -count))
        events.sort()
        load = 0
        for _, _, value in events:
            load += value
            if load > capacity:
                return False
        return True