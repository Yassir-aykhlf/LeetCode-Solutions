"""
Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n^2).
"""

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return heapq.nsmallest(k, [num for arr in matrix for num in arr])[-1]
        # n = len(matrix)
        # lo, hi = matrix[0][0], matrix[n - 1][n - 1]
        # while lo < hi:
        #     mid = (lo + hi) // 2
        #     count = 0
        #     row, col = 0, n - 1
        #     while row < n and col >= 0:
        #         if matrix[row][col] <= mid:
        #             count += col + 1
        #             row += 1
        #         else:
        #             col -= 1
        #     if count >= k:
        #         hi = mid
        #     else:
        #         lo = mid + 1
        # return hi
