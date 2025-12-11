class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = collections.Counter()
        target = collections.Counter(t)
        have, need = 0, len(target)
        min_len = float("inf")
        res = (0, 0)
        l = 0
        for r in range(len(s)):
            window[s[r]] += 1
            if s[r] in target and target[s[r]] == window[s[r]]:
                have += 1
            while have == need:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    res = (l, r + 1)
                if s[l] in target and target[s[l]] == window[s[l]]:
                    have -= 1
                window[s[l]] -= 1
                l += 1
        return s[res[0]: res[1]] if min_len != float("inf") else ""