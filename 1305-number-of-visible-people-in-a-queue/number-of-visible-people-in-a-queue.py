class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        res = [0] * len(heights)
        stack = []
        for i in range(len(heights)-1, -1, -1):
            count = 0
            while stack and stack[-1] < heights[i]:
                stack.pop()
                count += 1
            if stack:
                count += 1
            res[i] = count
            stack.append(heights[i]) 
        return res