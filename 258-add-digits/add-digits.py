class Solution:
    def addDigits(self, num: int) -> int:
        sum = 0
        while num > 0:
            sum += num % 10
            num //= 10
        while sum >= 10:
            n, d = divmod(sum, 10)
            sum = n + d
        return sum