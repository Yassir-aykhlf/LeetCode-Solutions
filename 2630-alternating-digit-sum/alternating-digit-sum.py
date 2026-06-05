class Solution:
    def alternateDigitSum(self, n: int) -> int:
        sign = 1
        nums = [int(n) for n in list(str(n))]
        res = 0
        for n in nums:
            res += n * sign
            sign = -1 if sign == 1 else 1
        return res