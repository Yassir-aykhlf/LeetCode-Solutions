class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, isqrt(c)
        while a <= b:
            res = a ** 2 + b ** 2
            if res == c:
                return True
            elif res < c:
                a += 1
            else:
                b -= 1
        return False