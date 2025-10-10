class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        k = n // 4
        min_len = float('inf')
        freq = Counter(s)
        excess = {num: count-k for num, count in freq.items() if count > k}
        if not excess:
            return 0
        window = defaultdict(int)
        have, need = 0, len(excess)
        l = 0
        for r in range(n):
            window[s[r]] += 1
            if s[r] in excess and window[s[r]] == excess[s[r]]:
                have += 1
            while have == need:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                if s[l] in excess and window[s[l]] == excess[s[l]]:
                    have -= 1
                window[s[l]] -= 1
                l += 1
        return min_len