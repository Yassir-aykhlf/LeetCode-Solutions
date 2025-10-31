class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len = 0
        state = {0:0, 1:0}
        l = 0
        for r in range(len(nums)):
            state[nums[r]] += 1
            while state[0] > k:
                state[nums[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len