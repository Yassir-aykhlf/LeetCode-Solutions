class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def BS(row):
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
        for row in matrix:
            if BS(row):
                return True
        return False