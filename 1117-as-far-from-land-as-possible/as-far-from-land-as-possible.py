class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        distance, water = 0, 0
        n = len(grid)
        dq = deque()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dq.append((r, c))
                else:
                    water += 1
        if len(dq) == n * n or not len(dq):
            return -1
        while dq and water:
            level_size = len(dq)
            for _ in range(level_size):
                row, col = dq.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < n and 0 <= nc < n and \
                        grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        water -= 1
                        dq.append((nr, nc))
            distance += 1
        return distance