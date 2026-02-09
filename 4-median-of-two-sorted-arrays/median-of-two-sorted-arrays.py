class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        comb = sorted(nums1 + nums2)
        return comb[len(comb) // 2] if len(comb) % 2 else sum(comb[len(comb) // 2 - 1 : len(comb) // 2 + 1]) / 2