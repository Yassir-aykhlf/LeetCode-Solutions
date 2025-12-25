class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        nums_sum = sum(nums)
        n = len(nums)
        if nums_sum < x: return -1
        if nums_sum == x: return n
        target = nums_sum - x
        max_len, cur, l = 0, 0, 0
        for r in range(n):
            cur += nums[r]
            while cur > target:
                cur -= nums[l]
                l += 1
            if cur == target:
                max_len = max(max_len, r - l + 1)
        return n - max_len if max_len else -1