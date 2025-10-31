class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        maximum_pair_sum = 0
        while l < r:
            maximum_pair_sum = max(maximum_pair_sum, nums[l] + nums[r])
            l += 1
            r -= 1
        return maximum_pair_sum