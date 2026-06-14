class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 1, n - 1
        def check(val):
            count = 0
            for n in nums:
                if n <= val:
                    count += 1
            return count
        while l < r:
            mid = (l + r) // 2
            if check(mid) > mid:
                r = mid
            else:
                l = mid + 1
        return l