class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        lo, hi = 1, max(bloomDay)
        ans = -1
        def check(days):
            flwrs = 0
            bqts = 0
            for b in bloomDay:
                if b <= days:
                    flwrs += 1
                    if flwrs == k:
                        flwrs = 0
                        bqts += 1
                else:
                    flwrs = 0
            return bqts >= m
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans