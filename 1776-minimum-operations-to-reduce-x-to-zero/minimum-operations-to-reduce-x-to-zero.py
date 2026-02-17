class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        sum_ = sum(nums)
        target_sum = sum_ - x
        if x == sum_: return len(nums)
        if sum_ < x: return -1
        longest_len = 0
        curr_sum = 0
        sum_idx = {0: -1}
        l = 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum > target_sum:
                curr_sum -= nums[l]
                l += 1
            if curr_sum == target_sum:
                longest_len = max(longest_len, r - l + 1)
        return len(nums) - longest_len if longest_len else -1