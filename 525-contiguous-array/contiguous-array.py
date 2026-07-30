class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        state = {0: -1}
        curr_sum = 0
        res = 0
        for i in range(len(nums)):
            curr_sum += 1 if nums[i] else -1
            if curr_sum in state:
                res = max(res, i - state[curr_sum])
            else:
                state[curr_sum] = i
        return res