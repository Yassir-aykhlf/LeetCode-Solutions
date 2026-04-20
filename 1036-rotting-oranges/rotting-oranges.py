class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        fresh = 0
        minutes = 0
        dq = deque()
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    dq.append((r, c))
        while dq and fresh:
            level_size = len(dq)
            for _ in range(level_size):
                row, col = dq.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < ROW and \
                        0 <= nc < COL and \
                        grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        dq.append((nr, nc))
            minutes += 1
        return minutes if not fresh else -1