class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_set = set()
        atlantic_set = set()
        m, n = len(heights), len(heights[0])
        
        def dfs(row, col, ocean_set, prev_height):
            if row < 0 or row >= m or \
                col < 0 or col >= n or \
                (row, col) in ocean_set or \
                heights[row][col] < prev_height:
                return
            ocean_set.add((row, col))
            dfs(row + 1, col, ocean_set, heights[row][col])            
            dfs(row - 1, col, ocean_set, heights[row][col])
            dfs(row, col + 1, ocean_set, heights[row][col])
            dfs(row, col - 1, ocean_set, heights[row][col])
        
        for row in range(0, m):
            dfs(row, 0, pacific_set, heights[row][0])
            dfs(row, n - 1, atlantic_set, heights[row][n - 1])
        for col in range(0, n):
            dfs(0, col, pacific_set, heights[0][col])
            dfs(m - 1, col, atlantic_set, heights[m - 1][col])

        return [list(coord) for coord in (pacific_set & atlantic_set)]