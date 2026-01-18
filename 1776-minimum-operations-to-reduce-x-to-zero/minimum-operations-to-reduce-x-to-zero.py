class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        total = sum(nums)
        target = total - x
        if total == x: return n
        if total < x: return -1
        curr_sum = 0
        max_len = 0
        l = 0
        for r in range(n):
            curr_sum += nums[r]
            while curr_sum > target:
                curr_sum -= nums[l]
                l += 1
            if curr_sum == target:
                max_len = max(max_len, r - l + 1)
        return n - max_len if max_len else -1