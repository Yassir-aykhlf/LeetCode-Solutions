class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        pac_set = set()
        atl_set = set()
        m, n = len(heights), len(heights[0])
        def dfs(r, c, _set, prev=float("-inf")):
            if not (
                0 <= r < m and
                0 <= c < n and
                (r, c) not in _set and
                heights[r][c] >= prev
            ):  return
            _set.add((r, c))
            dfs(r + 1, c, _set, heights[r][c])
            dfs(r - 1, c, _set, heights[r][c])
            dfs(r, c + 1, _set, heights[r][c])
            dfs(r, c - 1, _set, heights[r][c])
        for i in range(m):
            dfs(i, 0, pac_set)
            dfs(i, n-1, atl_set)
        for i in range(n):
            dfs(0, i, pac_set)
            dfs(m-1, i, atl_set)
        return list(pac_set & atl_set)