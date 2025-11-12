class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = isqrt(c)
        while a <= b:
            res = a*a + b*b
            if res == c:
                return True
            elif res < c:
                a += 1
            else:
                b -= 1
        return False