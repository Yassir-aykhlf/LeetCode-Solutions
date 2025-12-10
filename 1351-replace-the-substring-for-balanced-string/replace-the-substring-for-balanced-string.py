class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        k = n / 4
        window = collections.defaultdict(int)
        freq = collections.Counter(s)
        target = {char: count - k for char, count in freq.items() if count > k}
        if not target:
            return 0
        have, need = 0, len(target)
        min_len = float("inf")
        l = 0
        for r in range(n):
            window[s[r]] += 1
            if s[r] in target and target[s[r]] == window[s[r]]:
                have += 1
            while have == need:
                min_len = min(min_len, r - l + 1)
                if s[l] in target and target[s[l]] == window[s[l]]:
                    have -= 1
                window[s[l]] -= 1
                l += 1
        return min_len if min_len != float("inf") else 0