class Solution:
    """
    We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].
    You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time
    range.
    If you choose a job that ends at time X you will be able to start another job that starts at time X.
    """
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        dp_endtimes = [0]
        dp_profit = [0]
        for end_time, start_time, profit in jobs:
            last_job_idx = bisect.bisect_right(dp_endtimes, start_time) - 1
            current_profit = profit + dp_profit[last_job_idx]
            if current_profit > dp_profit[-1]:
                dp_endtimes.append(end_time)
                dp_profit.append(current_profit)
        return dp_profit[-1]