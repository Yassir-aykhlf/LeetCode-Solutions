class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        k = n // 4
        freq = collections.Counter(s)
        overflow = {char: count-k for char, count in freq.items() if count > k}
        if not overflow:
            return 0
        have, need = 0, len(overflow)
        window = collections.Counter()
        min_len = float('inf')
        l = 0
        for r in range(n):
            window[s[r]] += 1
            if s[r] in overflow and window[s[r]] == overflow[s[r]]:
                have += 1
            while have == need:
                min_len = min(min_len, r - l + 1)
                if s[l] in overflow and window[s[l]] == overflow[s[l]]:
                    have -= 1
                window[s[l]] -= 1
                l += 1
        return min_len if min_len != float('inf') else 0