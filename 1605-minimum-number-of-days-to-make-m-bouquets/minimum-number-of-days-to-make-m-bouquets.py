class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def check(day):
            flowers = 0
            bouquets = 0
            for b in bloomDay:
                if b <= day:
                    flowers += 1
                    if flowers == k:
                        flowers = 0
                        bouquets += 1
                else:
                    flowers = 0
            return bouquets >= m
        if len(bloomDay) < m * k:
            return -1
        lo, hi = min(bloomDay), max(bloomDay) # blooming range
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans