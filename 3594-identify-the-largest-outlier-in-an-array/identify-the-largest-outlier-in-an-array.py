class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        _max = float("-inf")
        _sum = sum(nums)
        _cun = collections.Counter(nums)
        for n in nums:
            rem = _sum - n
            if rem / 2 in _cun and (n != rem / 2 or _cun[n] > 1):
                _max = max(_max, n)
        return _max