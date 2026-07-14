class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        state = {0:0 , 1:0}
        l = 0
        res = 0
        for r in range(len(nums)):
            state[nums[r]] += 1
            while state[0] > k:
                state[nums[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res