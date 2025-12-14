class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        m, n = len(needle), len(haystack)
        if m > n:
            return -1
        mod = 10**9 + 7
        base = 26
        highest_pow = pow(base, m - 1, mod)
        n_hash, h_hash = 0, 0
        for i in range(m):
            n_hash = (n_hash * base + ord(needle[i])) % mod
            h_hash = (h_hash * base + ord(haystack[i])) % mod
        if n_hash == h_hash and haystack[:m] == needle:
            return 0
        for i in range(1, n - m + 1):
            old = ord(haystack[i - 1])
            new = ord(haystack[i + m - 1])
            h_hash = ((h_hash - old * highest_pow) * base + new) % mod
            if h_hash == n_hash and haystack[i : i+m] == needle:
                return i
        return -1