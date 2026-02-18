class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(capacity):
            days_taken = 1
            curr_weight = 0
            for w in weights:
                if curr_weight + w > capacity:
                    days_taken += 1
                    curr_weight = w
                else:
                    curr_weight += w
            return days_taken <= days
        lo, hi = max(weights), sum(weights)
        ans = hi
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans