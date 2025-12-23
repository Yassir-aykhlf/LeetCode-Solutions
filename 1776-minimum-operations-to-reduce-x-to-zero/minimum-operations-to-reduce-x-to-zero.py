class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total_sum = sum(nums)
        target = total_sum - x
        min_len = float("inf")
        n = len(nums)
        if target == 0:
            return n
        if target < 0:
            return -1
        curr = 0
        l = 0
        for r in range(len(nums)):
            curr += nums[r]
            while curr > target:
                curr -= nums[l]
                l += 1
            if curr == target:
                min_len = min(min_len, n - (r - l + 1))
        return min_len if min_len != float("inf") else -1