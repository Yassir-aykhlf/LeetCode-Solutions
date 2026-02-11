class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        odd = 1
        even = 0
        for n in nums:
            if n % 2:
                result[odd] = n
                odd += 2
            else:
                result[even] = n
                even += 2
        return result