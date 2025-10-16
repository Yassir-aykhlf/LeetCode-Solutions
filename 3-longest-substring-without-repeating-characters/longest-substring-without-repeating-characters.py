class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = collections.Counter()
        l = 0
        max_len = 0
        for r in range(len(s)):
            window[s[r]] += 1
            while s[r] in window and window[s[r]] > 1:
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len