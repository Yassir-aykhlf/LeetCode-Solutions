class Solution:
    def specialArray(self, nums: list[int]) -> int:
        l, r = 0, len(nums)
        while l <= r:
            mid = (l + r) // 2
            count = sum(1 for n in nums if n >= mid)
            if count == mid:
                return mid
            elif count > mid:
                l = mid + 1
            else:
                r = mid - 1
        return -1