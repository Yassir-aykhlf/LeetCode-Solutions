class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        lis = 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            lis = max(lis, dp[i])
        return lis