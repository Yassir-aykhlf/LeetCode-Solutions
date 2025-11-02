class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        wsum = 0
        min_len = float('inf')
        l = 0
        for r in range(n):
            wsum += nums[r]
            while wsum >= target:
                min_len = min(min_len, r - l + 1)
                wsum -= nums[l]
                l += 1
        return min_len if min_len != float('inf') else 0