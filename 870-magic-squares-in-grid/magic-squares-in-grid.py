class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        count = 0
        R, C = len(grid), len(grid[0])
        if R < 3 or C < 3:
            return 0
        def isMagical(r, c):
            val = [grid[r+i][c+j] for i in range(3) for j in range(3)]
            if set(val) != set(range(1, 10)):
                return False
            ref = sum(grid[r][c:c+3])
            # rows
            for i in range(3):
                if sum(grid[r + i][c:c+3]) != ref:
                    return False
            # cols
            for i in range(3):
                if sum(grid[r + j][c + i] for j in range(3)) != ref:
                    return False
            # diags
            d1, d2 = 0, 0
            for i in range(3):
                d1 += grid[r + i][c + i]
                d2 += grid[r + i][c + 2 - i]
            if d1 != ref or d2 != ref:
                return False
            return True
        for r in range(R - 2):
            for c in range(C - 2):
                count += 1 if isMagical(r, c) else 0
        return count