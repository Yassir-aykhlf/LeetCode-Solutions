class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        window = collections.defaultdict(int)
        window_sum = 0
        l = 0
        for r in range(len(nums)):
            window_sum += nums[r]
            while window_sum >= target:
                min_len = min(min_len, r - l + 1)
                window_sum -= nums[l]
                l += 1
        return min_len if min_len != float('inf') else 0