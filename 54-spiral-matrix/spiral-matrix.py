class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        r, c = 0, 0
        dr, dc = 0, 1
        visited = set()
        m, n = len(matrix), len(matrix[0])
        for i in range(m * n):
            res.append(matrix[r][c])
            visited.add((r, c))
            nr, nc = r + dr, c + dc
            if not (0 <= nc < n and 0 <= nr < m and (nr, nc) not in visited):
                dr, dc = dc, -dr
            r += dr
            c += dc
        return res