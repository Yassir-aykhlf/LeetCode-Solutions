class Solution:
    def balancedString(self, s: str) -> int:
        freq = collections.Counter(s)
        k = len(s) / 4
        target = {char: count - k for char, count in freq.items() if count > k}
        if not target:
            return 0
        window = collections.Counter()
        have, need = 0, len(target)
        res = float("inf")
        l = 0
        for r in range(len(s)):
            window[s[r]] += 1
            if s[r] in target and target[s[r]] == window[s[r]]:
                have += 1
            while have == need:
                res = min(res, r - l + 1)
                if s[l] in target and target[s[l]] == window[s[l]]:
                    have -= 1
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
        return res if res != float("inf") else 0