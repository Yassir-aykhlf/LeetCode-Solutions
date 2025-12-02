class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = isqrt(c)
        while l <= r:
            comb = l*l + r*r
            if comb == c:
                return True
            elif comb < c:
                l += 1
            else:
                r -= 1
        return False