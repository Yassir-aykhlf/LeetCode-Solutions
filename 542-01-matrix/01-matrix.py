class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dq = deque()
        ROW, COL = len(mat), len(mat[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for row in range(ROW):
            for col in range(COL):
                if mat[row][col] == 1:
                    mat[row][col] = -1
                else:
                    dq.append((row, col))
        while dq:
            level_size = len(dq)
            for i in range(level_size):
                r, c = dq.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROW and \
                        0 <= nc < COL and \
                        mat[nr][nc] == -1:
                        mat[nr][nc] = mat[r][c] + 1
                        dq.append((nr, nc))
        return mat