class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        count = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def bfs(row, col):
            if row < 0 or row >= ROW or \
                col < 0 or col >= COL or \
                (row, col) in visited or \
                not grid[row][col]:
                return
            visited.add((row, col))
            for dr, dc in directions:
                bfs(row + dr, col + dc)
        for row in range(ROW):
            bfs(row, 0)
            bfs(row, COL-1)
        for col in range(COL):
            bfs(0, col)
            bfs(ROW-1, col)
        for row in range(1, ROW-1):
            for col in range(1, COL-1):
                if grid[row][col] and (row, col ) not in visited:
                    count += 1
        return count