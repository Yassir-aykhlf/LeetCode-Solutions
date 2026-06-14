class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        def check(max_total):
            cuts = 1
            curr_sum = 0
            for n in nums:
                if curr_sum + n > max_total:
                    curr_sum = n
                    cuts += 1
                else:
                    curr_sum += n 
            return cuts <= k
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return r