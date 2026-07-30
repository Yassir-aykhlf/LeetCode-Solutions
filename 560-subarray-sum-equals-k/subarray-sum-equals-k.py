class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        state = {0: 1}
        count = 0
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            target = curr_sum - k
            if target in state:
                count += state[target]
            state[curr_sum] = state.get(curr_sum, 0) + 1
        return count