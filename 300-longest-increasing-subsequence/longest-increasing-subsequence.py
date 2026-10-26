class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        LIS = 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            LIS = max(LIS, dp[i])
        return LIS