class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        grid = [[0] * (m+1) for _ in range(n+1)]
        for i in range(n + 1):
            grid[i][m] = n - i
        for i in range(m + 1):
            grid[n][i] = m - i
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if word1[i] == word2[j]:
                    grid[i][j] = grid[i+1][j+1]
                else:
                    grid[i][j] = 1 + min(
                        grid[i+1][j],
                        grid[i][j+1],
                        grid[i+1][j+1]
                    )
        return grid[0][0]