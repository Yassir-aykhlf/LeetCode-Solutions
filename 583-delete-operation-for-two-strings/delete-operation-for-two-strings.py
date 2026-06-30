class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)
        grid = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        for i in range(len1 - 1, -1, -1):
            for j in range(len2 - 1, -1, -1):
                if word1[i] == word2[j]:
                    grid[i][j] = 1 + grid[i + 1][j + 1]
                else:
                    grid[i][j] = max(grid[i + 1][j], grid[i][j + 1])
        return len(word1) + len(word2) - (grid[0][0] * 2)