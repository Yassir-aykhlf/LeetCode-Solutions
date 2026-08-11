class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        _max = 0
        _state = collections.defaultdict(int)
        _len = len(nums)
        l = 0
        acc = 0
        for r in range(_len):
            _state[nums[r]] = _state.get(nums[r], 0) + 1
            acc += nums[r]
            while _state[nums[r]] > 1:
                _state[nums[l]] -= 1
                acc -= nums[l]
                l += 1
            _max = max(_max, acc)
        return _max