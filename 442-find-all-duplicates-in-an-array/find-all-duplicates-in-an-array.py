class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        nums_s = set(nums)
        for num in nums:
            if num in nums_s:
                nums_s.remove(num)
            else:
                res.append(num)
        return res