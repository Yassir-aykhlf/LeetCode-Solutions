class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x
        best = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            res = mid * mid
            if res == x:
                return mid
            elif res > x:
                hi = mid - 1
            else:
                best = mid
                lo = mid + 1
        return best