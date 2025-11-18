class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = -1
        closestD = float('inf') 
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                comb = nums[i] + nums[l] + nums[r]
                distance = abs(comb - target)
                if distance < closestD:
                    closestD = distance
                    res = comb
                if comb == target:
                    return target
                elif comb < target:
                    l += 1
                else:
                    r -= 1
        return res