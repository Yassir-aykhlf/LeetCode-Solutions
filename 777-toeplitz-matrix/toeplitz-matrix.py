class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(m - 1, 0, -1):
            for j in range(n - 1, -1, -1):
                cor_i = i - 1
                cor_j = j - 1
                if cor_i < 0 or cor_j < 0:
                    continue
                if matrix[i][j] != matrix[cor_i][cor_j]:
                    return False
        return True