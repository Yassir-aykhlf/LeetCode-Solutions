class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums_s = set(nums)
        res = []
        for num in nums:
            if num in nums_s:
                nums_s.remove(num)
            else:
                res.append(num)
        return res