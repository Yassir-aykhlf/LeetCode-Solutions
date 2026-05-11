class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_distance = float("inf")
        best_res = 0
        n = len(nums)
        for i in range(n - 2):
            a = i + 1
            b = n - 1
            while a < b:
                comb = nums[i] + nums[a] + nums[b]
                dist = abs(comb - target)
                if comb == target:
                    return comb
                if dist < closest_distance:
                    closest_distance = dist
                    best_res = comb
                if comb < target:
                    a += 1
                else:
                    b -= 1
        return best_res