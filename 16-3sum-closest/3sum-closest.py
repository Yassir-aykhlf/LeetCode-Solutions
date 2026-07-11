class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_dist = float('inf')
        closest_sum = -1
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            while l < r:
                comb = nums[i] + nums[l] + nums[r]
                dist = abs(target - comb)
                if comb == target:
                    return comb
                if dist < closest_dist:
                    closest_dist = dist
                    closest_sum = comb
                if comb < target:
                    l += 1
                else:
                    r -= 1
        return closest_sum