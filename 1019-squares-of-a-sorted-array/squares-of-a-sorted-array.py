class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        res = [0] * len(nums)
        w = r
        while l <= r:
            l_val = nums[l] ** 2
            r_val = nums[r] ** 2
            if l_val > r_val:
                res[w] = l_val
                l += 1
                w -= 1
            else:
                res[w] = r_val
                r -= 1
                w -= 1
        return res