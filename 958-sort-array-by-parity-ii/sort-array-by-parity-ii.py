class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        res = [0] * len(nums)
        o, e = 1, 0
        for i in range(len(nums)):
            if nums[i] % 2:
                res[o] = nums[i]
                o += 2
            else:
                res[e] = nums[i]
                e += 2
        return res