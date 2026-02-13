class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        state = [0] * (n + 1)
        for first, last, seats in bookings:
            state[first - 1] += seats
            state[last] -= seats
        res = []
        current = 0
        for seats in state[:-1]:
            current += seats
            res.append(current)
        return res