class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxs = collections.defaultdict(set)
        for row in range(9):
            for col in range(9):
                cell = board[row][col]
                if cell == '.':
                    continue
                box = (row // 3, col // 3)
                if (cell in rows[row] or
                    cell in cols[col] or
                    cell in boxs[box]):
                    return False
                rows[row].add(cell)
                cols[col].add(cell)
                boxs[box].add(cell)
        return True