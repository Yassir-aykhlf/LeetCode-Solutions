class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo, hi = max(weights), sum(weights)
        ans = hi
        def check(wei):
            days_taken = 1
            curr_weight = 0
            for w in weights:
                if w + curr_weight > wei:
                    days_taken += 1
                    curr_weight = w
                else:
                    curr_weight += w
            return days_taken <= days
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans