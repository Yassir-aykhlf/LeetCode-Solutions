class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            rightmost = (n & 1)
            n >>= 1
            result <<= 1
            result = result | rightmost
        return result