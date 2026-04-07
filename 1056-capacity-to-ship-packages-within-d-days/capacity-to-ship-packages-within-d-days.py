class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(cap):
            days_taken = 1
            curr_weight = 0
            for w in weights:
                if w + curr_weight > cap:
                    days_taken += 1
                    curr_weight = w
                else:
                    curr_weight += w
            return days_taken <= days
        lo, hi = max(weights), sum(weights)
        ans = lo
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans