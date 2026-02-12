class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # sort nums so the addition of the first element and the last is minimized
        nums.sort()
        # track max sum
        max_sum = 0
        l, r = 0, len(nums) - 1
        while l < r:
            max_sum = max(max_sum, nums[l] + nums[r])
            l += 1
            r -= 1
        return max_sum