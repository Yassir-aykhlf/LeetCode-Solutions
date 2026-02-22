class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available_rooms = [i for i in range(n)]
        heapq.heapify(available_rooms)
        used_rooms = []
        meeting_counts = [0] * n
        for start, end in meetings:
            while used_rooms and used_rooms[0][0] <= start:
                _, room = heapq.heappop(used_rooms)
                heapq.heappush(available_rooms, room)
            if available_rooms:
                room = heapq.heappop(available_rooms)
                heapq.heappush(used_rooms, (end, room))
                meeting_counts[room] += 1
            else:
                earliest_end, rooms = heapq.heappop(used_rooms)
                new_end = earliest_end + (end - start)
                heapq.heappush(used_rooms, (new_end, rooms))
                meeting_counts[rooms] += 1
        max_meetings = max(meeting_counts)
        return meeting_counts.index(max_meetings)