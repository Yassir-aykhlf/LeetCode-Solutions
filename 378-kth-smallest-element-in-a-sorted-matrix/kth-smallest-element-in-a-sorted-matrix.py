class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        l, r = matrix[0][0], matrix[n - 1][n - 1]
        while l <= r:
            mid = (l + r) // 2
            count, row, col = 0, 0, n - 1
            while row < n and col >= 0:
                if matrix[row][col] <= mid:
                    count += col + 1
                    row += 1
                else:
                    col -= 1
            if count < k:
                l = mid + 1
            else:
                r = mid - 1
        return l