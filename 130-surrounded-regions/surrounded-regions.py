class Solution:
    def solve(self, board: list[list[str]]) -> None:
        visited = set()
        m, n = len(board), len(board[0])
        def dfs(r, c):
            if not (
                0 <= r < m and
                0 <= c < n and
                board[r][c] == "O" and
                (r, c) not in visited
            ):  return
            visited.add((r, c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        for i in range(n):
            dfs(0, i)
            dfs(m-1, i)
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if board[i][j] == "O" and (i, j) not in visited:
                    board[i][j] = "X"