class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1
        while row < m and col >= 0:
            val = matrix[row][col]
            if val == target:
                return True
            elif val < target:
                row += 1
            else:
                col -= 1
        return False