class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = defaultdict(int)
        res = 0
        l = 0
        for r in range(len(s)):
            counter[s[r]] += 1
            while counter[s[r]] > 1:
                counter[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res