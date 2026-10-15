class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        min_set = {min(r) for r in matrix}
        max_set = {max(c) for c in zip(*matrix)}
        return list(min_set & max_set)