class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, isqrt(c)
        while l <= r:
            comb = l**2 + r**2
            if comb == c:
                return True
            elif comb > c:
                r -= 1
            else:
                l += 1
        return False