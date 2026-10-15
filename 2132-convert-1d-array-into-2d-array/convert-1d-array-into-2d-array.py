class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if len(original) != m * n:
            return []
        res = [[0] * n for _ in range(m)]
        for i in range(len(original)):
            res[i // n][i % n] = original[i]
        return res