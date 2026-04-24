class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        max_area = 0
        def bfs(row, col):
            if row < 0 or row >= ROW or \
                col < 0 or col >= COL or \
                not grid[row][col]:
                return 0
            grid[row][col] = 0
            return 1 + bfs(row-1,col) + bfs(row+1,col) + bfs(row,col-1) + bfs(row,col+1)
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col]:
                    max_area = max(max_area, bfs(row, col))
        return max_area