class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-count for count in count.values()]
        heapq.heapify(max_heap)
        time = 0
        dq = deque()
        while max_heap or dq:
            time += 1
            if max_heap:
                count = heapq.heappop(max_heap)
                count += 1
                if count != 0:
                    dq.append([count, time + n])
            if dq and dq[0][1] == time:
                wake_up_task_freq = dq.popleft()[0]
                heapq.heappush(max_heap, wake_up_task_freq)
        return time