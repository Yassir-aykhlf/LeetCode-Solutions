class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        max_area = 0
        row_cnt = len(grid)
        col_cnt = len(grid[0])
        visited = set()

        def dfs(row, col):
            if row < 0 or row >= row_cnt or \
               col < 0 or col >= col_cnt or \
               (row, col) in visited or \
               grid[row][col] == 0:
               return 0
            visited.add((row, col))
            return (1 +
                    dfs(row - 1, col) +
                    dfs(row + 1, col) +
                    dfs(row, col - 1) +
                    dfs(row, col + 1))

        for row in range(row_cnt):
            for col in range(col_cnt):
                if grid[row][col] == 1 and (row, col) not in visited:
                    area = dfs(row, col)
                    max_area = max(max_area, area)
        return max_area