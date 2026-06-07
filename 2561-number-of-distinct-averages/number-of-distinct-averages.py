class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        l = 0
        r = n - 1
        nums.sort()
        seen = set()
        while l < r:
            comb = nums[l] + nums[r]
            if comb not in seen:
                seen.add(comb)
                count += 1
            l += 1
            r -= 1
        return count