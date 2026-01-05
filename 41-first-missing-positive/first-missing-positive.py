class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        for i in range(len(nums)):
            index = abs(nums[i])
            if index > 0 and index <= n:
                if nums[index - 1] > 0:
                    nums[index - 1] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        return n + 1