class Solution:
    def balancedString(self, s: str) -> int:
        min_len = float("inf")
        n = len(s)
        k = n // 4
        window = defaultdict(int)
        freq = Counter(s)
        excess = {char: count - k for char, count in freq.items() if count > k}
        if not excess:
            return 0
        have, need = 0, len(excess)
        l = 0
        for r in range(n):
            window[s[r]] += 1
            if s[r] in excess and excess[s[r]] == window[s[r]]:
                have += 1
            while have == need:
                min_len = min(min_len, r - l + 1)
                if s[l] in excess and excess[s[l]] == window[s[l]]:
                    have -= 1
                window[s[l]] -= 1
                l += 1
        return min_len if min_len != float("inf") else 0