class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        res = [[0] * n for _ in range(n)]
        dr, dc = 0, 1
        r, c = 0, 0
        for i in range(n*n):
            res[r][c] = i + 1
            nr, nc = r + dr, c + dc
            if not (
                0 <= nr < n and
                0 <= nc < n and
                not res[nr][nc]
            ):  dr, dc = dc, -dr
            r += dr
            c += dc
        return res