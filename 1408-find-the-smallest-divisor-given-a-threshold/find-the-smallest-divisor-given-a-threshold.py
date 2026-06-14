class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        # why I chose r as max divisor: because this way max_sum = len(nums)? idk? let's see
        while l < r:
            mid = (l + r) // 2
            sum_ = 0
            for n in nums:
                sum_ += (n + mid - 1) // mid
            if sum_ <= threshold:
                r = mid
            else:
                l = mid + 1
        return r