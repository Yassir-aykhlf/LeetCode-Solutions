class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        def check(pair_dist):
            count = 0
            l = 0
            for r in range(len(nums)):
                while nums[r] - nums[l] > pair_dist:
                    l += 1
                count += r - l
            return count >= k
        lo, hi = 0, nums[-1] - nums[0]
        ans  = hi
        while lo <= hi:
            mid = (lo + hi) // 2 
            if check(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans