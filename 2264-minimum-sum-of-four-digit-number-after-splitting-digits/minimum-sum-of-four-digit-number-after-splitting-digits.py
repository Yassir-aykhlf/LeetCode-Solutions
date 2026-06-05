class Solution:
    def minimumSum(self, num: int) -> int:
        nums = []
        while num > 0:
            num, d = divmod(num, 10)
            nums.append(d)
        nums.sort()
        new1 = nums[0] * 10 + nums[-1]
        new2 = nums[1] * 10 + nums[-2]
        return new1 + new2