class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lowerBound(nums, target):
            lo, hi = 0, len(nums) - 1
            ans = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] >= target:
                    if nums[mid] == target:
                        ans = mid
                    hi = mid - 1
                elif nums[mid] < target:
                    lo = mid + 1
            return ans
        def upperBound(nums, target):
            lo, hi = 0, len(nums) - 1
            ans = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] <= target:
                    if nums[mid] == target:
                        ans = mid
                    lo = mid + 1
                elif nums[mid] > target:
                    hi = mid - 1
            return ans
        return [lowerBound(nums, target), upperBound(nums, target)]