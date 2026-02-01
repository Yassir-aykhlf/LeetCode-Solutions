class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        lo, hi = max(nums), sum(nums)
        def can_split(capacity):
            count = 1
            cur_sum = 0
            for num in nums:
                if cur_sum + num > capacity:
                    count += 1
                    cur_sum = num
                else:
                    cur_sum += num
            return count <= k
        while lo < hi:
            mid = (lo + hi) // 2
            if can_split(mid):
                hi = mid
            else:
                lo = mid + 1
        return hi