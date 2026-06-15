class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        def check(cap):
            time_taken = 0
            for p in piles:
                time_taken += (p + cap - 1) // cap
            return time_taken <= h
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return r