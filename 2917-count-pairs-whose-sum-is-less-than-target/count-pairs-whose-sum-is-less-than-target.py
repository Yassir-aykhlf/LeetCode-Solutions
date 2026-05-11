class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        l, r = 0, len(nums) - 1
        while l < r:
            comb = nums[l] + nums[r]
            if comb >= target:
                r -= 1
            else:
                count += (r - l)
                l += 1
        return count