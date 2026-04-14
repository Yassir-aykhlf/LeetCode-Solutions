class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        m, n = len(grid), len(grid[0])
        visited = set()
        def dfs(row, col):
            if row < 0 or row >= m or \
                col < 0 or col >= n or \
                (row, col) in visited or \
                grid[row][col] == 0:
                return 0
            visited.add((row, col))    
            return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and (row, col) not in visited:
                    max_area = max(max_area, dfs(row, col))
        return max_area