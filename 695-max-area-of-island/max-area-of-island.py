class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        res = 0
        def dfs(r, c):
            if not (
                0 <= r < m and
                0 <= c < n and
                grid[r][c] and
                (r, c) not in visited
            ):  return 0
            visited.add((r, c))
            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
        for r in range(m):
            for c in range(n):
                res = max(res, dfs(r, c))
        return res