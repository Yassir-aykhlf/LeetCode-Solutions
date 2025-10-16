class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        for f in range(n - 1, 1, -1):
            a = 0
            b = f - 1
            while a < b:
                res = nums[a] + nums[b]
                if res > nums[f]:
                    count += b - a
                    b -= 1
                else:
                    a += 1
        return count