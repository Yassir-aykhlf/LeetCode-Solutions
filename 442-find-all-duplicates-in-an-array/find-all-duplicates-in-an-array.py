class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                res.append(nums[i])
        return res