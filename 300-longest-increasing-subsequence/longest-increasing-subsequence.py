class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        lis = [1] * n
        res = -1
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    lis[i] = max(lis[i], lis[j] + 1)
            res = max(res, lis[i])
        return res