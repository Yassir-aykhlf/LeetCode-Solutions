class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return sorted([item for sub in matrix for item in sub])[k - 1]