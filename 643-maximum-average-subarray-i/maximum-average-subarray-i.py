class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = window_sum = sum(nums[:k])
        for r in range(k, len(nums)):
            window_sum += nums[r] - nums[r - k]
            max_sum = max(max_sum, window_sum)
        return max_sum / k