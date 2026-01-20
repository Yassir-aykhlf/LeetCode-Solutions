class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, len(matrix) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        row = matrix[hi]
        lo, hi = 0, len(row) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False