class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        events = sorted(zip(endTime, startTime, profit))
        dp_endtime = [0]
        dp_profit = [0]
        for end, start, profit in events:
            last_event_idx = bisect.bisect_right(dp_endtime, start) - 1
            current_profit = dp_profit[last_event_idx] + profit
            if current_profit > dp_profit[-1]:
                dp_profit.append(current_profit)
                dp_endtime.append(end)
        return dp_profit[-1]