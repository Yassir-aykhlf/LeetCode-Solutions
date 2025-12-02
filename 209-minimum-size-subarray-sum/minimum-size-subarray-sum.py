class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float("inf")
        cur_sum = 0
        l = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            while cur_sum >= target:
                min_len = min(min_len, r -l + 1)
                cur_sum -= nums[l]
                l += 1
        return min_len if min_len != float("inf") else 0