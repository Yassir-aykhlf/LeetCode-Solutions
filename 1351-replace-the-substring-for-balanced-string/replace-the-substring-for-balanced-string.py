class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        k = n // 4
        freq = collections.Counter(s)
        excess = {char: count-k for char, count in freq.items() if count > k}
        if not excess:
            return 0
        window = collections.Counter()
        have = 0
        need = len(excess)
        min_len = float('inf')
        l = 0
        for r in range(len(s)):
            window[s[r]] += 1
            if s[r] in excess and window[s[r]] == excess[s[r]]:
                have += 1
            while have == need:
                min_len = min(min_len, r - l + 1)
                if s[l] in excess and window[s[l]] == excess[s[l]]:
                    have -= 1 
                window[s[l]] -= 1
                l += 1
        return min_len if min_len != float('inf') else 0