class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        count = 0
        nums.sort()
        for i in range(len(nums) - 1, -1, -1):
            l, r = 0, i - 1
            while l < r:
                comb = nums[l] + nums[r]
                if comb > nums[i]:
                    count += r - l
                    r -= 1
                else:
                    l += 1
        return count