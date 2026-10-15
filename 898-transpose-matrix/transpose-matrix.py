class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        return list(zip(*matrix))