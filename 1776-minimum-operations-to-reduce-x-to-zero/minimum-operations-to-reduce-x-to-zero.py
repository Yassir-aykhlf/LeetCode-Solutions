class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        _sum = sum(nums)
        target = _sum - x
        _len = len(nums)
        if _sum == x:
            return _len
        l = 0
        acc = 0
        _max = -1
        seen = {0: -1}
        for r in range(_len):
            acc += nums[r]
            if acc - target in seen:
                _max = max(_max, r - seen[acc-target] + 1)
            seen[acc] = r
        return _len - _max + 1 if _max != -1 else -1