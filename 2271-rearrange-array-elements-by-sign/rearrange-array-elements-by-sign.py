class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        positive, negative = 0, 1
        for n in nums:
            if n > 0:
                res[positive] = n
                positive += 2
            else:
                res[negative] = n
                negative += 2
        return res