class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = collections.defaultdict(int)
        max_len = 0
        n = len(s)
        l = 0
        for r in range(n):
            char = s[r]
            window[char] += 1
            while window[char] > 1:
                window[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len