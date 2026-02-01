class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        cost = [0] * 3
        cost[0] = nums[0]
        rem = sorted(nums[1:])
        cost[1], cost[2] = rem[0], rem[1]
        return sum(cost)