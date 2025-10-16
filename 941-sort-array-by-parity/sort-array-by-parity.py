class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        odd = 0
        even = n - 1
        res = [0] * n
        for num in nums:
            if num % 2 != 0:
                res[even] = num
                even -= 1
            else:
                res[odd] = num
                odd += 1
        return res