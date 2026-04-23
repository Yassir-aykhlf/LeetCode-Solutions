class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            ( 0, -1),          ( 0, 1),
            ( 1, -1), ( 1, 0), ( 1, 1)
        ]
        distance = 1
        dq = deque([(0, 0)])
        visited = {(0, 0)}
        while dq:
            level_size = len(dq)
            for _ in range(level_size):
                row, col = dq.popleft()
                if row == n-1 and col == n-1 and grid[row][col] == 0:
                    return distance
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < n and 0 <= nc < n and \
                        grid[nr][nc] == 0 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        dq.append((nr, nc))
            distance += 1
        return -1