class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
        A_len, B_len = len(A), len(B)
        total_len = A_len + B_len
        half = total_len // 2
        lo, hi = 0, A_len - 1
        while True:
            i = (lo + hi) // 2
            j = half - (i + 1) - 1
            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i + 1] if i + 1 < A_len else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j + 1] if j + 1 < B_len else float('inf')
            if Aleft <= Bright and Bleft <= Aright:
                if total_len % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                hi = i - 1
            elif Bleft > Aright:
                lo = i + 1
