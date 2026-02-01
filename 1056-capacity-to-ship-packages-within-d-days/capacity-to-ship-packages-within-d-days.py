class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(max_capacity):
            days_taken = 1
            cur_sum = 0
            for w in weights:
                if cur_sum + w > max_capacity:
                    days_taken += 1
                    cur_sum = w
                else:
                    cur_sum += w
            return days_taken <= days
        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return hi