class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        count = 0
        def dfs(r, c):
            if not (
                0 <= r < m and 
                0 <= c < n and
                grid[r][c] == "1" and
                (r, c) not in visited
            ):  return
            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and (r, c) not in visited:
                    count += 1
                    dfs(r, c)
        return count