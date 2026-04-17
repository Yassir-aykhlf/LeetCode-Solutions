class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_ocean = set()
        a_ocean = set()
        ROW, COL = len(heights), len(heights[0])

        def dfs(row, col, ocean, prev_height):
            if row < 0 or row >= ROW or \
                col < 0 or col >= COL or \
                (row, col) in ocean or \
                heights[row][col] < prev_height:
                return
            ocean.add((row, col))
            dfs(row + 1, col, ocean, heights[row][col])
            dfs(row - 1, col, ocean, heights[row][col])
            dfs(row, col + 1, ocean, heights[row][col])
            dfs(row, col - 1, ocean, heights[row][col])

        for row in range(ROW):
            dfs(row, 0, p_ocean, heights[row][0])
            dfs(row, COL - 1, a_ocean, heights[row][COL - 1])
        for col in range(COL):
            dfs(ROW - 1, col, a_ocean, heights[ROW - 1][col])
            dfs(0, col, p_ocean, heights[0][col])
        
        return [list(coord) for coord in (p_ocean & a_ocean)]