class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = 1
        even = 0
        n = len(nums)
        res = [0] * n
        for num in nums:
            if num % 2 == 0:
                res[even] = num
                even += 2
            else:
                res[odd] = num
                odd += 2
        return res