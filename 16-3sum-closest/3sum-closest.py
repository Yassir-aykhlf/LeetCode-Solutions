class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        n = len(nums)
        closest = float("inf")
        best = 0
        nums.sort()
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                comb = nums[i] + nums[l] + nums[r]
                if comb == target:
                    return comb
                dist = abs(target - comb)
                if dist < closest:
                    closest = dist
                    best = comb
                if comb < target:
                    l += 1
                else:
                    r -= 1
        return best