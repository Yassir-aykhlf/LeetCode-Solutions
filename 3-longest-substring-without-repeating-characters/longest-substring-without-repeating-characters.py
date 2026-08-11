class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        state = defaultdict(int)
        _len = len(s)
        _max = 0
        l = 0
        for r in range(_len):
            state[s[r]] += 1
            while state[s[r]] > 1:
                state[s[l]] -= 1
                l += 1
            _max = max(_max, r - l + 1)
        return _max