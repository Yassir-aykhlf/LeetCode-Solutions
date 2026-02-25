class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        change = [0] * (n + 2)
        for first, last, seats in bookings:
            change[first] += seats
            change[last + 1] -= seats
        load = 0
        res = []
        for i in change[1:]:
            load += i
            res.append(load)
        return res[:-1]