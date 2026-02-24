class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # upper bound
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return hi