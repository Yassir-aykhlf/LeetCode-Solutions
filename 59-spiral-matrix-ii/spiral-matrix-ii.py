class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        res = [[0] * n for _ in range(n)]
        r, c = 0, 0
        dr, dc = 0, 1
        for i in range(1, n * n + 1):
            res[r][c] = i
            nr, nc = r + dr, c + dc
            if not (0 <= nr < n and 0 <= nc < n and res[nr][nc] == 0):
                dr, dc = dc, -dr
            r += dr
            c += dc
        return res