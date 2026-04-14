class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        count = 0
        def dfs(row, col):
            if row < 0 or row >= m or \
                col < 0 or col >= n or \
                (row, col) in visited or \
                grid[row][col] == "0":
                return
            visited.add((row, col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1" and (row, col) not in visited:
                    dfs(row, col)
                    count += 1
        return count