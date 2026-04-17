class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, minutes = 0, 0
        ROW, COL = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dq = deque()
        
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    dq.append((row, col))

        while dq and fresh:
            level_size = len(dq)
            for i in range(level_size):
                rr, rc = dq.popleft()
                for dr, dc in directions:
                    nr, nc = rr + dr, rc + dc
                    if 0 <= nr < ROW and \
                        0 <= nc < COL and \
                        grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        dq.append((nr, nc))
            minutes += 1
        
        return minutes if not fresh else -1