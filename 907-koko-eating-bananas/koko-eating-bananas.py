class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(daily_rate):
            hours_taken = 0
            for p in piles:
                if p <= daily_rate:
                    hours_taken += 1
                else:
                    hours_taken += math.ceil(p / daily_rate)
            return hours_taken <= h
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return hi