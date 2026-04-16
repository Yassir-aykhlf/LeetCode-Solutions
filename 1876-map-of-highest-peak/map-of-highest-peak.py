class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(isWater), len(isWater[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dq = deque()
        for r in range(ROW):
            for c in range(COL):
                if isWater[r][c] == 1:
                    dq.append((r, c))
                    isWater[r][c] = 0
                else:
                    isWater[r][c] = -1
        while dq:
            level_size = len(dq)
            for i in range(level_size):
                r, c = dq.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if 0 <= row < ROW and \
                        0 <= col < COL and \
                        isWater[row][col] == -1:
                        isWater[row][col] = isWater[r][c] + 1
                        dq.append((row, col))
        return isWater