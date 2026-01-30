class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """ O(Nlogn); 29 ms; 23.92% """
        # return heapq.nsmallest(k, sorted([num for arr in matrix for num in arr]))[-1]
        n = len(matrix)
        lo, hi = matrix[0][0], matrix[n - 1][n - 1]
        while lo < hi:
            mid = (lo + hi) // 2
            count = 0
            row, col = 0, n - 1
            while row < n and col >= 0:
                if matrix[row][col] <= mid:
                    count += col + 1
                    row += 1
                else:
                    col -= 1
            if count >= k:
                hi = mid
            else:
                lo = mid + 1
        return hi