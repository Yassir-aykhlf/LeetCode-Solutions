class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(capacity):
            count = 1
            curr_sum = 0
            for num in nums:
                if curr_sum + num > capacity:
                    count += 1
                    curr_sum = num
                    if count > k:
                        return False
                else:
                    curr_sum += num
            return True
        lo, hi = max(nums), sum(nums)
        res = hi
        while lo <= hi:
            capacity = (lo + hi) // 2
            if check(capacity):
                res = capacity
                hi = capacity - 1
            else:
                lo = capacity + 1
        return res