class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        non_dups = set(nums)
        res = []
        for num in nums:
            if num in non_dups:
                non_dups.remove(num)
            else:
                res.append(num)
        return res