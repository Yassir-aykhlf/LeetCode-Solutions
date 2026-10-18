class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        r, c = 0, 0
        dr, dc = 0, 1
        mat = [[0] * n for _ in range(n)]
        for i in range(1, n * n + 1):
            mat[r][c] = i
            nr, nc = r + dr, c + dc
            if not (
                0 <= nr < n and 
                0 <= nc < n and
                not mat[nr][nc]
            ):  dr, dc = dc, -dr
            r += dr
            c += dc
        return mat