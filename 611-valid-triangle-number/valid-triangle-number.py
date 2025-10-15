class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for f in range(len(nums) - 1, 1, -1):
            r = f - 1
            l = 0
            while l < r:
                res = nums[l] + nums[r]
                if res > nums[f]:
                    count += r - l
                    r -= 1
                else:
                    l += 1
        return count