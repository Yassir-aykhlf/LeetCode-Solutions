class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        window = defaultdict(int)
        l = 0
        max_len = 0
        for r in range(len(s)):
            window[s[r]] += 1
            while window[s[r]] > 2:
                window[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len