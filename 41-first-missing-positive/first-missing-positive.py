class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        max_ = max(nums)
        nums_s = set(nums)
        for num in range(1 , max_ + 1):
            if num not in nums_s:
                return num
        return max_ + 1 if max_>= 1 else 1