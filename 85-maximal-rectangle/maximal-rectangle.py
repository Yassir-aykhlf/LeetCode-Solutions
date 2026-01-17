class Solution:
    def maxRec(self, nums: List[int]) -> int:
        max_area = 0
        stack = []
        for i, num in enumerate(nums):
            start = i
            while stack and stack[-1][1] > num:
                idx, pre = stack.pop()
                max_area = max(max_area, pre * (i - idx))
                start = idx
            stack.append((start, num))
        for i, num in stack:
            max_area = max(max_area, num * (len(nums) - i))
        return max_area
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        cols = [0] * m
        max_area = 0
        for row in range(n):
            for col in range(m):
                cols[col] = cols[col] + 1 if matrix[row][col] == "1" else 0
            max_area = max(max_area, self.maxRec(cols))
        return max_area