class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lower_bound = -1
        upper_bound = -1
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] >= target:
                if nums[mid] == target:
                    lower_bound = mid
                hi = mid - 1
            else:
                lo = mid + 1
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] <= target:
                if nums[mid] == target:
                    upper_bound = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return [lower_bound, upper_bound]