class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        res = [[0] * (n - 2) for _ in range(n - 2)]
        for r in range(n - 2):
            for c in range(n - 2):
                max_ = float("-inf")
                for i in range(3):
                    for j in range(3):
                        max_ = max(max_, grid[r+i][c+j])
                res[r][c] = max_
        return res