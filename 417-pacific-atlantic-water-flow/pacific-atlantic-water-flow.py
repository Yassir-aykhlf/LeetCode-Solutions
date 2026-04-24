class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        pacific_set = set()
        atlantic_set = set()
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def bfs(row, col, ocean_set, prev_height):
            if row < 0 or row >= ROW or \
                col < 0 or col >= COL or \
                (row, col) in ocean_set or \
                heights[row][col] < prev_height:
                return
            ocean_set.add((row, col))
            for dr, dc in direction:
                bfs(row + dr, col + dc, ocean_set, heights[row][col])
        for row in range(ROW):
            bfs(row, 0, pacific_set, heights[row][0])
            bfs(row, COL-1, atlantic_set, heights[row][COL-1])
        for col in range(COL):
            bfs(0, col, pacific_set, heights[0][col])
            bfs(ROW-1, col, atlantic_set, heights[ROW-1][col])
        return [list(coord) for coord in (pacific_set & atlantic_set)]