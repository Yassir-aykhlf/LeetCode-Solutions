class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(sum):
            # can make at least k subarrays
            curr_sum = 0
            splits = 1
            for r in range(len(nums)):
                if curr_sum + nums[r] > sum:
                    splits += 1
                    curr_sum = nums[r]
                else:
                    curr_sum += nums[r]
            return splits <= k
        
        lo, hi = max(nums), sum(nums)
        ans = hi
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans