class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        def check(pair_res):
            l = 0
            count = 0
            for r in range(len(nums)):
                while nums[r] - nums[l] > pair_res:
                    l += 1
                count += r - l
            return count >= k
        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return hi