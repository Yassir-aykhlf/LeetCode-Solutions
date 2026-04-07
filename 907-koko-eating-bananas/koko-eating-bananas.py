class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            hours_taken = 0
            for p in piles:
                if p <= k:
                    hours_taken += 1
                else:
                    hours_taken += math.ceil(p / k)
            return hours_taken <= h
        # what is our search range? [1, max(piles)]
        lo, hi = 1, max(piles)
        ans = hi
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans