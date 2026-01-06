class Solution:
    def maxRec(self, cols):
        stack = []
        max_area = 0
        for i, h in enumerate(cols):
            start = i
            while stack and stack[-1][1] > h:
                idx, hei = stack.pop()
                max_area = max(max_area, hei * (i - idx))
                start = idx
            stack.append((start, h))
        for i, h in stack:
            max_area = max(max_area, h *(len(cols) - i))
        return max_area
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        max_area = 0
        n = len(matrix)
        m = len(matrix[0])
        cols = [0] * m
        for row in range(n):
            for col in range(m):
                cols[col] = cols[col] + 1 if matrix[row][col] == "1" else 0
            max_area = max(max_area, self.maxRec(cols))
        return max_area