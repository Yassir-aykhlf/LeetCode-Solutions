class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, 1
        max_gap = 0
        while r < len(nums):
            max_gap = max(max_gap, nums[r] - nums[l])
            l += 1
            r += 1
        return max_gap