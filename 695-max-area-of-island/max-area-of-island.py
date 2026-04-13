class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        row, col = 0, 0
        max_area = 0
        visited = set()
        def dfs(row, col):
            if row < 0 or row >= n or \
                col < 0 or col >= m or \
                (row, col) in visited or \
                grid[row][col] == 0:
                return 0
            visited.add((row, col))
            return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)
        for row in range(n):
            for col in range(m):
                if (row, col) not in visited and \
                    grid[row][col] == 1:
                    max_area = max(max_area, dfs(row, col))
        return max_area