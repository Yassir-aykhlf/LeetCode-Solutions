class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = collections.defaultdict(int)
        max_len = 0
        l = 0
        for r in range(len(s)):
            seen[s[r]] += 1
            while seen[s[r]] > 1:
                seen[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len