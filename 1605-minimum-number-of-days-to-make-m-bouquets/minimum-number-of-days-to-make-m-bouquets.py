class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def check(min_days):
            bouquets = 0
            flowers = 0
            for b in bloomDay:
                if b <= min_days:
                    flowers += 1
                    if flowers == k:
                        flowers = 0
                        bouquets += 1
                else:
                    flowers = 0
            return bouquets >= m
        ans = -1
        lo, hi = min(bloomDay), max(bloomDay)
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans