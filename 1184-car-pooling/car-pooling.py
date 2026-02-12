class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # events: list[tuples(location, operation, value)]
        events = []
        for count, start, end in trips:
            events.append((start, 1, count))
            events.append((end, 0, -count))
        events.sort()
        on_board = 0
        for location, _, value in events:
            on_board += value
            if on_board > capacity:
                return False
        return True