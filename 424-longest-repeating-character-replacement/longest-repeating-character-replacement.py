class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        freq = collections.Counter()
        l = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            while r - l + 1 - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len