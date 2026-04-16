class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dq = deque()
        distance = 0
        water, land = 0, 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    water += 1
                else:
                    dq.append((r, c))
        if len(dq) == 0 or len(dq) == ROW * COL:
            return -1
        while dq:
            level_size = len(dq)
            for i in range(level_size):
                r, c = dq.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if 0 <= row < ROW and \
                       0 <= col < COL and \
                       grid[row][col] == 0:
                       grid[row][col] = 1
                       dq.append((row, col))
            distance += 1
        return distance - 1