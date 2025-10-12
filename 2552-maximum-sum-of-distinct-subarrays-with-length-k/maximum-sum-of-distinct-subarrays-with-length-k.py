class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        window = nums[:k]
        window_sum = sum(window)
        window_state = collections.Counter(window)
        max_sum = 0
        if len(window_state) == k:
            max_sum = window_sum
        for r in range(k, n):
            window_state[nums[r]] += 1
            window_state[nums[r - k]] -= 1
            window_sum += nums[r]
            window_sum -= nums[r - k]
            if window_state[nums[r - k]] == 0:
                del window_state[nums[r - k]]
            if len(window_state) == k:
                max_sum = max(max_sum, window_sum)
        return max_sum