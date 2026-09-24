class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        res = [0] * len(nums)
        for i, n in enumerate(nums):
            res[i] = nums[nums[i]]
        return res