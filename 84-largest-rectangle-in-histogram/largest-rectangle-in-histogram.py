class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                idx, val = stack.pop()
                max_area = max(max_area, val * (i - idx))
                start = idx
            stack.append((start, height))
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area