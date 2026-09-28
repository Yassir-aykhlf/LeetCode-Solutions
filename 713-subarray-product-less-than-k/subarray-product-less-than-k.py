class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        acc = 1
        if k < 1:
            return 0
        res = 0
        l = 0
        for r in range(len(nums)):
            acc *= nums[r]
            while acc > k:
                acc //= nums[l]
                l += 1
            if acc < k:
                res += (r - l + 1)
        return res