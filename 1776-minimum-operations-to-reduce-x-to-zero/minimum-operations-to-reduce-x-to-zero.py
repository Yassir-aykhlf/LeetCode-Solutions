class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        num_sum = sum(nums)
        tar_sum = num_sum - x
        if num_sum < x: return -1
        if num_sum == x: return n
        max_del = 0
        curr = 0
        l = 0
        for r in range(len(nums)):
            curr += nums[r]
            while curr > tar_sum:
                curr -= nums[l]
                l += 1
            if curr == tar_sum:
                max_del = max(max_del, r - l + 1)
        return n - max_del if max_del else -1