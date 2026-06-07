class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        count = 0
        nums1.sort()
        nums2.sort()
        for i in range(len(nums1)):
            l = 0
            r = len(nums2) - 1
            target = nums1[i] ** 2
            while l < r:
                prod = nums2[l] * nums2[r]
                if prod == target:
                    if nums2[l] == nums2[r]:
                        count += (r - l + 1) * (r - l) // 2
                        l = r
                        continue
                    l_count = 1
                    while l < r and nums2[l] == nums2[l + 1]:
                        l += 1
                        l_count += 1
                    r_count = 1
                    while l < r and nums2[r] == nums2[r - 1]:
                        r -= 1
                        r_count += 1
                    count += l_count * r_count
                    l += 1
                    r -= 1
                elif prod < target:
                    l += 1
                else:
                    r -= 1
        for i in range(len(nums2)):
            l = 0
            r = len(nums1) - 1
            target = nums2[i] ** 2
            while l < r:
                prod = nums1[l] * nums1[r]
                if prod == target:
                    if nums1[l] == nums1[r]:
                        count += (r - l + 1) * (r - l) // 2
                        l = r
                        continue
                    l_count = 1
                    while l < r and nums1[l] == nums1[l + 1]:
                        l += 1
                        l_count += 1
                    r_count = 1
                    while l < r and nums1[r] == nums1[r - 1]:
                        r -= 1
                        r_count += 1
                    count += l_count * r_count
                    l += 1
                    r -= 1
                elif prod < target:
                    l += 1
                else:
                    r -= 1
        return count