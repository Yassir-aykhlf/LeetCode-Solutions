class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closestD = float('inf')
        result = 0
        n = len(nums)
        nums.sort()
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            while l < r:
                comb = nums[i] + nums[l] + nums[r]
                if comb == target:
                    return comb
                distance = abs(comb - target)
                if distance < closestD:
                    closestD = distance
                    result = comb
                if comb < target:
                    l += 1
                else:
                    r -= 1
        return result