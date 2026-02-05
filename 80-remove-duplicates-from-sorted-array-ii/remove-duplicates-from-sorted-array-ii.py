class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 2
        w = 2
        for i in range(2, len(nums)):
            if nums[w - 2] != nums[i]:
                nums[w] = nums[i]
                w += 1
        return w