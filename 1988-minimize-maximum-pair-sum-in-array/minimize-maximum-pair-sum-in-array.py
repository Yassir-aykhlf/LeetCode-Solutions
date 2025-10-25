class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        max_pair = 0
        l, r = 0, n - 1
        while l < r:
            max_pair = max(nums[l] + nums[r], max_pair)
            l += 1
            r -= 1
        return max_pair