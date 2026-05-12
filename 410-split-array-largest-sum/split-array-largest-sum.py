class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        lo, hi = max(nums), sum(nums)
        ans = hi
        def check(sum_):
            splits = 1
            curr_sum = 0
            for n in nums:
                if curr_sum + n > sum_:
                    curr_sum = n
                    splits += 1
                else:
                    curr_sum += n
            return splits <= k
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans