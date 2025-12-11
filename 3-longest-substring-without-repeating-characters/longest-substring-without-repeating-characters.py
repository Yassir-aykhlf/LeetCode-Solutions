class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        window = defaultdict(int)
        for r in range(len(s)):
            window[s[r]] += 1
            while window[s[r]] > 1:
                window[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len