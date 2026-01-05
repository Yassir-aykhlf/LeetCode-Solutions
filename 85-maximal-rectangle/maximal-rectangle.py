class Solution:
    def maxHistogram(self, arr):
        stack = []
        max_area = 0
        for i, h in enumerate(arr):
            start = i
            while stack and stack[-1][1] > h:
                idx, hi = stack.pop()
                max_area = max(max_area, hi * (i - idx))
                start = idx
            stack.append((start, h))
        for i, h in stack:
            max_area = max(max_area, h * (len(arr) - i))
        return max_area
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        max_area = 0
        n = len(matrix)
        m = len(matrix[0])
        cols = [0] * m
        for row in range(n):
            for col in range(m):
                cols[col] = cols[col] + 1 if matrix[row][col] == "1" else 0
            max_area = max(max_area, self.maxHistogram(cols))
        return max_area