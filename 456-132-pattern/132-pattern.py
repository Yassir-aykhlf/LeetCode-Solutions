class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        third = float('-inf')
        stack = []
        for n in reversed(nums):
            if n < third:
                return True
            while stack and stack[-1] < n:
                third = stack.pop()
            stack.append(n)
        return False