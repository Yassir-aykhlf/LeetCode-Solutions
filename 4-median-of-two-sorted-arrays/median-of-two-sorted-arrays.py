class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(nums1) > len(nums2):
            A, B = B, A
        A_len, B_len = len(A), len(B)
        total = A_len + B_len
        half = total // 2
        lo, hi = 0, A_len - 1
        while True:
            i = (lo + hi) // 2
            j = half - (i + 1) - 1
            A_left = A[i] if i >= 0 else float('-inf')
            A_right = A[i + 1] if i + 1 < A_len else float('inf')
            B_left = B[j] if j >= 0 else float('-inf')
            B_right = B[j + 1] if j + 1 < B_len else float('inf')
            if A_left <= B_right and B_left <= A_right:
                if total % 2:
                    return min(A_right, B_right)
                return (max(A_left, B_left) + min(A_right, B_right)) / 2
            if A_left > B_right:
                hi = i - 1
            else:
                lo = i + 1