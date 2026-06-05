class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def isEven(n):
            count = 0
            while n > 0:
                n //= 10
                count += 1
            return not count % 2    
        return sum(1 for n in nums if isEven(n))