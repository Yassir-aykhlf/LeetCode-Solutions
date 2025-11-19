class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = 0
        odd = len(nums) - 1
        res = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                res[even] = nums[i]
                even += 1
            else:
                res[odd] = nums[i]
                odd -= 1
        return res