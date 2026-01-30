class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return heapq.nsmallest(k, sorted([num for arr in matrix for num in arr]))[-1]