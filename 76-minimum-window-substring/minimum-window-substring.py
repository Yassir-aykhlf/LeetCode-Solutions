class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_len = float("inf")
        ref = Counter(t)
        window = defaultdict(int)
        have, need = 0, len(ref)
        l = 0
        res = (0, 0)
        for r in range(len(s)):
            window[s[r]] += 1
            if s[r] in ref and ref[s[r]] == window[s[r]]:
                have += 1
            while have == need:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    res = (l, r + 1)
                if s[l] in ref and ref[s[l]] == window[s[l]]:
                    have -= 1
                window[s[l]] -= 1
                l += 1
        return s[res[0]: res[1]] if min_len != float("inf") else ""