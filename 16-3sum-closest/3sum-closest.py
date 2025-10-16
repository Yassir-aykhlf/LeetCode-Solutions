class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        closestD = float('inf')
        result = float('inf')
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            a = i + 1
            b = n - 1
            while a < b:
                comb = nums[i] + nums[a] + nums[b]
                if comb == target:
                    return comb
                distance = abs(comb - target)
                if distance < closestD:
                    closestD = distance
                    result = comb
                if comb < target:
                    a += 1
                else:
                    b -= 1
        return result