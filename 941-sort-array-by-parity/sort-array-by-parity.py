class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        res = [0] * len(nums)
        for n in nums:
            if n % 2:
                res[j] = n
                j -= 1
            else:
                res[i] = n
                i += 1
        return res