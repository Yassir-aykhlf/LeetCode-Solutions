class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        distance = 0
        land = 0
        dq = deque()
        ROW, COL = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 1:
                    dq.append((row, col))
                else:
                    land += 1
        if len(dq) == ROW * COL or len(dq) == 0:
            return -1
        while dq and land:
            level_size = len(dq)
            for i in range(level_size):
                lr, lc = dq.popleft()
                for dr, dc in directions:
                    nr, nc = lr + dr, lc + dc
                    if 0 <= nr < ROW and \
                        0 <= nc < COL and \
                        grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        dq.append((nr, nc))
                        land -= 1
            distance += 1
        return distance