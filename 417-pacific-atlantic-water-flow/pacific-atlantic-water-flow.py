class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()
        def dfs(row, col, reachable_set, prev_height):
            if row < 0 or row >= m or \
                col < 0 or col >= n or \
                (row, col) in reachable_set or \
                heights[row][col] < prev_height:
                return
            curr_height = heights[row][col]
            reachable_set.add((row, col))
            dfs(row + 1, col, reachable_set, curr_height)
            dfs(row - 1, col, reachable_set, curr_height)
            dfs(row, col + 1, reachable_set, curr_height)
            dfs(row, col - 1, reachable_set, curr_height)
            
        for col in range(n):
            dfs(0, col, pacific_reachable, heights[0][col])
        for row in range(m):
            dfs(row, 0, pacific_reachable, heights[row][0])

        for col in range(n):
            dfs(m - 1, col, atlantic_reachable, heights[m - 1][col])
        for row in range(m):
            dfs(row, n - 1, atlantic_reachable, heights[row][n - 1])

        return [list(coord) for coord in (pacific_reachable & atlantic_reachable)]