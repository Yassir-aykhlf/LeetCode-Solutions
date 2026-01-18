class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(goal):
            if goal < 0:
                return 0
            curr_sum = 0
            count = 0
            l = 0
            for r in range(len(nums)):
                curr_sum += nums[r]
                while curr_sum > goal:
                    curr_sum -= nums[l]
                    l += 1
                count += r - l + 1
            return count
        return atMost(goal) - atMost(goal - 1)