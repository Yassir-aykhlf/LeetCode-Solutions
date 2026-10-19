class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        pac_set = set()
        atl_set = set()
        m, n = len(heights), len(heights[0])
        bl, tr = (m - 1, 0), (0, n - 1)
        def dfs(coor, prev, _set):
            r, c = coor
            if not (
                0 <= r < m and
                0 <= c < n and
                (r, c) not in _set and
                heights[r][c] >= prev
            ):  return
            curr = heights[r][c]
            _set.add((r, c))
            dfs((r + 1, c), curr, _set)
            dfs((r - 1, c), curr, _set)
            dfs((r, c + 1), curr, _set)
            dfs((r, c - 1), curr, _set)
        for r in range(m):
            dfs((r, 0), float("-inf"), pac_set)
        for c in range(n):
            dfs((0, c), float("-inf"), pac_set)
        for r in range(m):
            dfs((r, n - 1), float("-inf"), atl_set)
        for c in range(n):
            dfs((m - 1, c), float("-inf"), atl_set)
        return list(pac_set & atl_set)