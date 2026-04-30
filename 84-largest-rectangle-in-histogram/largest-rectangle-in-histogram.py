class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, hei = stack.pop()
                max_area = max(max_area, hei * (i - idx))
                start = idx
            stack.append([start, h])
        for i, h in stack:
            max_area = max(max_area, (len(heights) - i) * h)
        return max_area