class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findBound(isFirst):
            lo, hi = 0, len(nums) - 1
            bound = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    bound = mid
                    if isFirst:
                        hi = mid - 1
                    else:
                        lo = mid + 1
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return bound
        return [findBound(True), findBound(False)]