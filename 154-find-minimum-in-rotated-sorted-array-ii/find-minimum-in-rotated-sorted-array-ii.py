class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[lo] == nums[mid] == nums[hi]:
                hi -= 1
                lo += 1
            elif nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[hi]