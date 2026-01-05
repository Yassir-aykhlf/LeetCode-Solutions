class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        mapping = {}
        for num in nums2:
            while stack and stack[-1] < num:
                mapping[stack.pop()] = num 
            stack.append(num)
        return [mapping.get(n, -1) for n in nums1]