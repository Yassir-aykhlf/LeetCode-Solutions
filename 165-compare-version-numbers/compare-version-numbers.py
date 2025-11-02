class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = [int(num) for num in version1.split('.')]
        nums2 = [int(num) for num in version2.split('.')]
        p1, p2 = 0, 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] > nums2[p2]:
                return 1
            elif nums2[p2] > nums1[p1]:
                return -1
            p1 += 1
            p2 += 1
        while p1 < len(nums1):
            if nums1[p1] > 0:
                return 1
            p1 += 1
        while p2 < len(nums2):
            if nums2[p2] > 0:
                return -1
            p2 += 1
        return 0