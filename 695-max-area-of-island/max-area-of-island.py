class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])
        visited = set()
        def dfs(r, c):
            if not (
                0 <= r < m and
                0 <= c < n and
                (r, c) not in visited and 
                grid[r][c]
            ):  return 0
            visited.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(m):
            for c in range(n):
                if grid[r][c] and (r, c) not in visited:
                    res = max(res, dfs(r, c))
        return res