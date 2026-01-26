class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return sorted([num for arr in matrix for num in arr])[k - 1]