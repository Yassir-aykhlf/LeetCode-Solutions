class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        closest = float("inf")
        res = 0
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                comb = nums[i] + nums[l] + nums[r]
                dist = abs(target - comb)
                if dist < closest:
                    closest = dist
                    res = comb
                if comb == target:
                    return comb 
                elif comb < target:
                    l += 1
                else:
                    r -= 1
        return res
                