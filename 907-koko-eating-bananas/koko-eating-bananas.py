class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            hours_need = 0
            for p in piles:
                hours_need += math.ceil(p / k)
            return hours_need <= h
        lo, hi = 1, max(piles)
        while lo <= hi:
            k = (lo + hi) // 2
            if check(k):
                min_k = k
                hi = k - 1
            else:
                lo = k + 1
        return min_k