class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        res = []
        mins = set()
        for row in matrix:
            mins.add(min(row))
        for c in range(len(matrix[0])):
            max_ = 0
            for r in range(len(matrix)):
                max_ = max(max_, matrix[r][c])
            if max_ in mins:
                res.append(max_)
        return res