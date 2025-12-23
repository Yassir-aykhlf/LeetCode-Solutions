class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if sum(nums) < x: return -1
        target = sum(nums) - x
        min_len = float("inf")
        n = len(nums)
        curr = 0
        l = 0
        for r in range(len(nums)):
            curr += nums[r]
            while curr > target:
                print(curr)
                curr -= nums[l]
                l += 1
            if curr == target:
                min_len = min(min_len, n - (r - l + 1))
        return min_len if min_len != float("inf") else -1