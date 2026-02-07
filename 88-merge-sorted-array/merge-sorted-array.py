class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        r = len(nums1) - 1
        m -= 1
        n -= 1
        while r >= 0 and m >= 0 and n >= 0:
            if nums2[n] > nums1[m]:
                nums1[r] = nums2[n]
                n -= 1
            else:
                nums1[r] = nums1[m]
                m -= 1
            r -= 1
        while r >= 0 and n >= 0:
            nums1[r] = nums2[n]
            n -= 1
            r -= 1
        while r >= 0 and m >= 0:
            nums1[r] = nums1[m]
            m -= 1
            r -= 1