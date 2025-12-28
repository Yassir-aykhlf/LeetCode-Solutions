class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        total_sum = sum(nums)
        target = total_sum - x
        if target == 0:
            return n
        if total_sum < x:
            return -1
        # looking for the max window with sum target
        max_len = 0
        curr = 0
        l = 0
        for r in range(n):
            curr += nums[r]
            while curr > target:
                curr -= nums[l]
                l += 1
            if curr == target:
                max_len = max(max_len, r - l + 1)
        return n - max_len if max_len else -1