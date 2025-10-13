class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = isqrt(c)
        while l <= r:
            result = l * l + r * r
            if result == c:
                return True
            elif result < c:
                l += 1
            else:
                r -= 1
        return False