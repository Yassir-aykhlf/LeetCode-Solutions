class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(mat), len(mat[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dq = deque()
        visited = set()
        for row in range(ROW):
            for col in range(COL):
                if mat[row][col] == 0:
                    dq.append((row, col))
                else:
                    mat[row][col] = -1
        while dq:
            row, col = dq.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < ROW and 0 <= nc < COL and \
                    (nr, nc) not in visited and \
                    mat[nr][nc] != 0:
                    visited.add((nr, nc))
                    dq.append((nr, nc))
                    mat[nr][nc] = mat[row][col] + 1
        return mat