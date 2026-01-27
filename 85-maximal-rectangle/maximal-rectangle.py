class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        def maxHisto(cols):
            max_area = 0
            stack = []
            for i, h in enumerate(cols):
                start = i
                while stack and stack[-1][1] > h:
                    idx, hi = stack.pop()
                    max_area = max(max_area, hi * (i - idx))
                    start = idx
                stack.append((start, h))
            for i, h in stack:
                max_area = max(max_area, h * (len(cols) - i))
            return max_area
        m, n = len(matrix), len(matrix[0])
        cols = [0] * n
        max_area = 0
        for row in range(m):
            for col in range(n):
                cols[col] = cols[col] + 1 if matrix[row][col] == "1" else 0
            max_area = max(max_area, maxHisto(cols))
        return max_area