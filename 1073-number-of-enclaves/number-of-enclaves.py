class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        count = 0
        visited = set()
        ROW, COL = len(grid), len(grid[0])
        
        def dfs(row, col):
            if row < 0 or row >= ROW or \
                col < 0 or col >= COL or \
                (row, col) in visited or \
                grid[row][col] == 0:
                return
            visited.add((row, col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(ROW):
            if grid[row][0]:
                dfs(row, 0)
            if grid[row][COL - 1]:
                dfs(row, COL - 1)
        for col in range(COL):
            if grid[0][col]:
                dfs(0, col)
            if grid[ROW - 1][col]:
                dfs(ROW - 1, col)
        
        for row in range(1, ROW - 1):
            for col in range(1, COL - 1):
                if grid[row][col] and (row, col) not in visited:
                    count += 1
        
        return count