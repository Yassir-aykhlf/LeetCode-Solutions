class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        min_left = nums[0]
        for num in nums[1:]:
            while stack and stack[-1][0] <= num:
                stack.pop()
            if stack and stack[-1][1] < num:
                return True
            stack.append((num, min_left))
            min_left = min(min_left, num)
        return False