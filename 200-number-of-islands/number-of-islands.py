class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = set()
        ROW, COL = len(grid), len(grid[0])
        def dfs(row, col):
            if row < 0 or row >= ROW or \
                col < 0 or col >= COL or \
                (row, col) in visited or \
                grid[row][col] == "0":
                return
            visited.add((row, col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1" and (r, c) not in visited:
                    count += 1
                    dfs(r, c)
        return count