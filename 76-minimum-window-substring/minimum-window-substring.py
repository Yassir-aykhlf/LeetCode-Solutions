class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = ""
        target = collections.Counter(t)
        window = collections.Counter()
        min_len = float('inf')
        have, need = 0, len(target)
        l = 0
        for r in range(len(s)):
            window[s[r]] += 1
            if s[r] in target and window[s[r]] == target[s[r]]:
                have += 1
            while have == need:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    result = s[l:r+1]
                if s[l] in target and window[s[l]] == target[s[l]]:
                    have -= 1
                window[s[l]] -= 1
                l += 1
        return result