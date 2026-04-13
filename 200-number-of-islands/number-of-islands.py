class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        row, col = 0, 0
        visited = set()
        count = 0
        def dfs(row, col):
            if row >= n or row < 0 or col >= m or col < 0 or \
                (row, col) in visited or \
                grid[row][col] == "0":
                return
            visited.add((row, col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(n):
            for col in range(m):
                if (row, col) not in visited and \
                    grid[row][col] == "1":
                    count += 1
                    dfs(row, col)
        return count