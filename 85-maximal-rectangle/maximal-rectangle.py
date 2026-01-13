class Solution:
    def maxRec(self, heights: List) -> int:
        res = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, hi = stack.pop()
                res = max(res, hi * (i - idx))
                start = idx
            stack.append((start, h))
        for i, h in stack:
            res = max(res, h * (len(heights) - i))
        return res
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        max_area = 0
        n = len(matrix)
        m = len(matrix[0])
        cols = [0] * m
        for row in range(n):
            for col in range(m):
                cols[col] = cols[col] + 1 if matrix[row][col] == "1" else 0
            max_area = max(max_area, self.maxRec(cols))
        return max_area