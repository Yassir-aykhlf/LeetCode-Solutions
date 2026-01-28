class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        comb = sorted(nums1 + nums2)
        return comb[len(comb) // 2] if len(comb) % 2 else (comb[len(comb) // 2 - 1] + comb[len(comb) // 2]) / 2
        # A, B = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        # A_len, B_len = len(A), len(B)
        # total = A_len + B_len
        # half  = total // 2
        # lo, hi = 0, A_len - 1
        # while True:
        #     i = (lo + hi) // 2
        #     j = half - (i + 1) - 1
        #     Aleft = A[i] if i >= 0 else float('-inf')
        #     Aright = A[i + 1] if i + 1 < A_len else float('inf')
        #     Bleft = B[j] if j >= 0 else float('-inf')
        #     Bright = B[j + 1] if j + 1 < B_len else float('inf')
        #     if Aleft <= Bright and Bleft <= Aright:
        #         if total % 2:
        #             return min(Aright, Bright)
        #         return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        #     elif Aleft > Bright:
        #         hi = i - 1
        #     else:
        #         lo = i + 1