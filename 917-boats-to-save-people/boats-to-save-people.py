class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        nums = people
        nums.sort()
        l = 0
        r = len(nums) - 1
        count = 0
        while l <= r:
            weight = nums[l] + nums[r]
            if weight <= limit:
                l += 1
            count += 1
            r -= 1
        return count