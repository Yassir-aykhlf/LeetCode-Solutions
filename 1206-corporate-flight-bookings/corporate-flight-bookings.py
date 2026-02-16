class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # O(N ^ 2) unacceptable for (2 * 10 ^ 4) size data
        # answer = [0] * n
        # for first, last, seats in bookings:
        #     for i in range(first-1, last):
        #         answer[i] += seats
        # return answer

        # O(N) solution, sweeping line
        answer = [0] * n
        events = [0] * (n + 2)
        for first, last, seats in bookings:
            events[first] += seats
            events[last + 1] -= seats
        current = 0
        for i in range(n):
            current += events[i+1]
            answer[i] = current
        return answer