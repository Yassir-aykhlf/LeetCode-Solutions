class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        seen = set()
        for num in nums1:
            seen.add(num)
        for num in nums2:
            if num in seen:
                result.add(num)
        return list(result)