class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        pac_set = set()
        atl_set = set()
        R, C = len(heights), len(heights[0])
        def dfs(r, c, set_, prev=float("-inf")):
            if not (
                0 <= r < R and
                0 <= c < C and
                (r, c) not in set_ and
                heights[r][c] >= prev
            ):  return
            set_.add((r, c))
            v = heights[r][c]
            dfs(r+1, c, set_, v)
            dfs(r-1, c, set_, v)
            dfs(r, c+1, set_, v)
            dfs(r, c-1, set_, v)

        for i in range(R):
            dfs(i, 0, pac_set)
            dfs(i, C-1, atl_set)
        for i in range(C):
            dfs(0, i, pac_set)
            dfs(R-1, i, atl_set)
        
        return list(pac_set & atl_set)