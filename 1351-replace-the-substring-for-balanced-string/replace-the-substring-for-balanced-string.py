class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        k = n // 4
        freq =collections.Counter(s)
        window = collections.defaultdict(int)
        excess = {char: count-k for char, count in freq.items() if count > k}
        if not excess:
            return 0
        have, need = 0, len(excess)
        min_len = float('inf')
        l = 0
        for r in range(n):
            window[s[r]] += 1
            if s[r] in excess and window[s[r]] == excess[s[r]]:
                have += 1
            while have == need:
                min_len = min(min_len, r - l + 1)
                if s[l] in excess and window[s[l]] == excess[s[l]]:
                    have -= 1
                window[s[l]] -= 1
                l += 1
        return min_len