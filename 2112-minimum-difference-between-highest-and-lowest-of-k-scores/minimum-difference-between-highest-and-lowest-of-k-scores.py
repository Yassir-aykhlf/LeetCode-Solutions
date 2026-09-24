class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()
        min_diff = nums[k - 1] - nums[0]
        for i in range(k, len(nums)):
            min_diff = min(min_diff, nums[i] - nums[i - k + 1])
        return min_diff