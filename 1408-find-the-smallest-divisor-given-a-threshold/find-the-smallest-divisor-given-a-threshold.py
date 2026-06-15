class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        def check(divisor):
            sum_ = 0
            for n in nums:
                sum_ += (n + divisor - 1) // divisor
            return sum_ <= threshold
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return r