class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return heapq.nsmallest(k, [num for arr in matrix for num in arr])[-1]
        
        # return sorted([num for arr in matrix for num in arr])[k - 1]

        # n = len(matrix)
        # lo, hi = matrix[0][0], matrix[n - 1][n - 1]
        # ans = hi
        # while lo <= hi:
        #     mid = (lo + hi) // 2
        #     row, col = 0, n - 1
        #     count = 0
        #     while row < n and col >= 0:
        #         if matrix[row][col] <= mid:
        #             count += col + 1
        #             row += 1
        #         else:
        #             col -= 1
        #     if count >= k:
        #         ans = mid
        #         hi = mid - 1
        #     else:
        #         lo = mid + 1
        # return ans