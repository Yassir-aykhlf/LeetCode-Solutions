class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        count = 0
        def dfs(row, col):
            if row < 0 or row >= m or \
                col < 0 or col >= n or \
                grid[row][col] == 0 or \
                (row, col) in visited:
                return
            visited.add((row, col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        
        for row in range(m):
            if grid[row][0] == 1 and (row, 0) not in visited:
                dfs(row, 0)
            if grid[row][n - 1] == 1 and (row, n - 1) not in visited:
                dfs(row, n - 1)

        for col in range(n):
            if grid[0][col] == 1 and (0, col) not in visited:
                dfs(0, col)
            if grid[m - 1][col] == 1 and (m - 1, col) not in visited:
                dfs(m - 1, col)

        for row in range(1, m - 1):
            for col in range(1, n - 1):
                if grid[row][col] == 1 and (row, col) not in visited:
                    count += 1
        return count