class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                prev_i, prev_h = stack.pop()
                max_area = max(max_area, prev_h * (i - prev_i))
                start = prev_i
            stack.append((start, h))
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area