class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        cols = [0] * m
        max_area = 0
        def maxRec(cols):
            stack = []
            max_area = 0
            for i, c in enumerate(cols):
                start = i
                while stack and stack[-1][1] > c:
                    idx, val = stack.pop()
                    max_area = max(max_area, val * (i - idx))
                    start = idx
                stack.append((start, c))
            for i, c in stack:
                max_area = max(max_area, c * (len(cols) - i))
            return max_area
        for row in range(n):
            for col in range(m):
                cols[col] = cols[col] + 1 if matrix[row][col] == "1" else 0
            max_area = max(max_area, maxRec(cols))
        return max_area