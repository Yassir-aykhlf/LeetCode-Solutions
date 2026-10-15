class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        w, r = 0, 0
        while r < len(nums):
            if nums[r]:
                nums[w] = nums[r]
                w += 1
            r += 1
        while w < len(nums):
            nums[w] = 0
            w += 1