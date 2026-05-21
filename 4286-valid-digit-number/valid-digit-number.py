class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        res = False
        while n > 0:
            if n < 10 and n == x:
                return False
            r = n % 10
            if r == x:
                res = True
            n = n // 10
        return res