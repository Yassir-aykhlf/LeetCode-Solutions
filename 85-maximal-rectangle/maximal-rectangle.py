class Solution:
    def maxHisto(self, nums):
        stack = []
        max_area = 0
        for i, h in enumerate(nums):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                start = index
                max_area = max(max_area, height * (i - index))
            stack.append((start, h))
        for i, h in stack:
            max_area = max(max_area, h * (len(nums) - i))
        return max_area
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        cols = [0] * n
        max_area = 0
        for row in range(m):
            for col in range(n):
                cols[col] = cols[col] + 1 if matrix[row][col] != "0" else 0
            max_area = max(max_area, self.maxHisto(cols))
        return max_area