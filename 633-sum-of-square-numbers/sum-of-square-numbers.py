class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squares = set()
        for num in range(isqrt(c) + 1):
            squares.add(num*num)
        for b_squared in squares:
            a_squared = c - b_squared
            if a_squared in squares:
                return True
        return False