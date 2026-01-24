class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        def check(hourly_rate):
            hours_taken = 0
            for p in piles:
                if p <= hourly_rate:
                    hours_taken += 1
                else:
                    hours_taken += math.ceil(p / hourly_rate)
            return hours_taken <= h
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo