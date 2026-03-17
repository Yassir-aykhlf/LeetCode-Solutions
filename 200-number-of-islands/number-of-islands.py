class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row_cnt = len(grid)
        col_cnt = len(grid[0])
        visited = set()
        island_cnt = 0

        def dfs(row, col):
            if row < 0 or row >= row_cnt or \
               col < 0 or col >= col_cnt or \
               (row, col) in visited or \
               grid[row][col] == "0":
               return
            visited.add((row, col))
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        for row in range(row_cnt):
            for col in range(col_cnt):
                if grid[row][col] == "1" and (row, col) not in visited:
                    dfs(row, col)
                    island_cnt += 1
        return island_cnt