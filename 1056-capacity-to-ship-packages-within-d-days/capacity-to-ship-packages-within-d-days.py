class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(daily_weight):
            days_taken = 1
            current_sum = 0
            for w in weights:
                if current_sum + w > daily_weight:
                    days_taken += 1
                    current_sum = 0
                current_sum += w
            return days_taken <= days
        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return hi