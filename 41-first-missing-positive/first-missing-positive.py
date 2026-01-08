class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] < 1 or nums[i] > n:
                nums[i] = n + 1
        for i in range(n):
            idx = abs(nums[i]) - 1
            if idx >= 0 and idx < n:
                if nums[idx] > 0:
                    nums[idx] *= -1
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1