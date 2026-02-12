class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        events = [0] * (n + 2)
        for first, last, seats in bookings:
            events[first] += seats
            events[last + 1] -= seats
        res = []
        current_seats = 0
        for seats in events[1:]:
            current_seats += seats
            res.append(current_seats)
        return res[:-1]