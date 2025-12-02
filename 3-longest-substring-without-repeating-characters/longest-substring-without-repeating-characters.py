class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = collections.defaultdict(int)
        max_len = 0
        l = 0
        for r in range(len(s)):
            while s[r] in window:
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
            window[s[r]] += 1
            max_len = max(max_len, r - l + 1)
        return max_len