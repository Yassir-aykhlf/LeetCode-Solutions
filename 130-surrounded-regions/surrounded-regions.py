class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        visited = set()
        def dfs(row, col):
            if row < 0 or row >= m or \
                col < 0 or col >= n or \
                (row, col) in visited or \
                board[row][col] == "X":
                return
            visited.add((row, col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)            
        for r in range(m):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][n - 1] == "O":
                dfs(r, n - 1)
        for c in range(n):
            if board[0][c] == "O":
                dfs(0, c)
            if board[m - 1][c] == "O":
                dfs(m - 1, c)
        for row in range(1, m - 1):
            for col in range(1, n - 1):
                if board[row][col] == "O" and (row, col) not in visited:
                    board[row][col] = "X"