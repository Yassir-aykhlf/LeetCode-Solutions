class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        lis = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    lis[i] = max(lis[i], lis[j] + 1)
        return max(lis)