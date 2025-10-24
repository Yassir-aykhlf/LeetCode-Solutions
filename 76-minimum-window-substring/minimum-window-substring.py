class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = collections.Counter(t)
        window = collections.defaultdict(int)
        min_len = float('inf')
        l = 0
        have, need = 0, len(target)
        res = (0, 0)
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
        return s[res[0]: res[1]]