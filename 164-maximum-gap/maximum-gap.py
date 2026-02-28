class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        a, b = 0, 1
        max_gap = 0
        while b < len(nums):
            max_gap = max(max_gap, nums[b] - nums[a])
            a += 1
            b += 1
        return max_gap