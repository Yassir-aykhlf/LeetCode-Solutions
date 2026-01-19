class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        y_lo, y_hi = 0, len(matrix) - 1
        while y_lo <= y_hi:
            mid = (y_lo + y_hi) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                y_lo = mid + 1
            else:
                y_hi = mid - 1
        target_y = y_hi
        target_row = matrix[target_y]
        lo, hi = 0, len(target_row) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if target_row[mid] == target:
                return True
            elif target_row[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False