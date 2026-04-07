class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in set(nums):
            return [-1, -1]
        return [bisect.bisect_left(nums, target), bisect.bisect_right(nums, target) - 1]