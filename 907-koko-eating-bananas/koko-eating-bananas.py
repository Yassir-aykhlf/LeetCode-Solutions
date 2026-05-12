class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        res = hi
        def check(rate):
            time = 0
            for p in piles:
                if p <= rate:
                    time += 1
                else:
                    time += ceil(p / rate)
            return time <= h
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return res