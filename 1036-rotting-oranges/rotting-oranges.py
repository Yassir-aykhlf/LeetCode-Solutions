class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        fresh, minutes = 0, 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dq = deque()
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    dq.append((r,c))
        while dq and fresh > 0:
            level_size = len(dq)
            for i in range(level_size):
                rr, rc = dq.popleft()
                for dr, dc in directions:
                    row, col = rr + dr, rc + dc
                    if 0 <= row < ROW and \
                       0 <= col < COL and \
                       grid[row][col] == 1:
                       grid[row][col] = 2
                       fresh -= 1
                       dq.append((row, col))
            minutes += 1
        return minutes if fresh == 0 else -1