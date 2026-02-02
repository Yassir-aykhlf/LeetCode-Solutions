class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        dp_end_times = [0]
        dp_profits = [0]
        for e, s, p in jobs:
            idx = bisect.bisect_right(dp_end_times, s) - 1
            # max profit just before current job
            current_profit = p + dp_profits[idx]
            if current_profit > dp_profits[-1]:
                dp_end_times.append(e)
                dp_profits.append(current_profit)
        return dp_profits[-1]