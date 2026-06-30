class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        len1 = len(nums1)
        len2 = len(nums2)
        grid = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        for i in range(len1 - 1, -1, -1):
            for j in range(len2 - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    grid[i][j] = 1 + grid[i + 1][j + 1]
                else:
                    grid[i][j] = max(grid[i+1][j], grid[i][j + 1])
        return grid[0][0]