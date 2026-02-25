class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def check(days):
            flowers = 0
            bouquets = 0
            for b in bloomDay:
                if b <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
            return bouquets >= m
        lo, hi = min(bloomDay), max(bloomDay)
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans