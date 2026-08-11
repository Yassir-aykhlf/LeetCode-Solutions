class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        _state = defaultdict(int)
        l = 0
        _max = 0
        _len = len(s)
        for r in range(_len):
            _state[s[r]] += 1
            while ((r - l + 1) - max(_state.values())) > k:
                _state[s[l]] -= 1
                l += 1
            _max = max(_max, r - l + 1)
        return _max