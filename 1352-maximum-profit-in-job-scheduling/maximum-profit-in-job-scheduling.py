class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        dp_endtime = [0]
        dp_profit = [0]
        for e, s, p in jobs:
            idx = bisect.bisect_right(dp_endtime, s) - 1
            current_profit = dp_profit[idx] + p
            if current_profit > dp_profit[-1]:
                dp_profit.append(current_profit)
                dp_endtime.append(e)
        return dp_profit[-1]