class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(mat), len(mat[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dq = deque()
        for r in range(ROW):
            for c in range(COL):
                if mat[r][c] == 0:
                    dq.append((r, c))
                else:
                    mat[r][c] = -1
        while dq:
            level_size = len(dq)
            for i in range(level_size):
                r, c = dq.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if 0 <= row < ROW and \
                       0 <= col < COL and \
                       mat[row][col] == -1:
                       mat[row][col] = mat[r][c] + 1
                       dq.append((row, col))
        return mat