class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = float("inf")
        best = -1
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                comb = nums[i] + nums[l] + nums[r]
                dest = abs(target - comb)
                if dest < closest:
                    closest = dest
                    best = comb
                if comb == target:
                    return target
                elif comb < target:
                    l += 1
                else:
                    r -= 1
        return best