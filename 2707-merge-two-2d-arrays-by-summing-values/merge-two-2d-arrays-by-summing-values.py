class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        nums1_h = {}
        for id, val in nums1:
            nums1_h[id] = val
        nums2_h = {**nums1_h}
        for id, val in nums2:
            if id in nums1_h:
                nums2_h[id] = nums1_h[id] + val
            else:
                nums2_h[id] = val
        return sorted([[id, val] for id, val in nums2_h.items()])