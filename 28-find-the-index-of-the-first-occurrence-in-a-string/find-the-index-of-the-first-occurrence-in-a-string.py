class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle)

        # n, m = len(haystack), len(needle)
        # for i in range(n - m + 1):
        #     if haystack[i: i + m] == needle:
        #         return i
        # return -1

        n, m = len(haystack), len(needle)
        if not needle: return 0
        if m > n: return -1
        MOD = 10**9 + 7
        BASE = 26
        highest_pow = pow(BASE, m - 1, MOD)
        n_hash = 0
        h_hash = 0
        for i in range(m):
            n_hash = (n_hash * BASE + (ord(needle[i]) - ord('a'))) % MOD
            h_hash = (h_hash * BASE + (ord(haystack[i]) - ord('a'))) % MOD
        if n_hash == h_hash:
            if haystack[:m] == needle:
                return 0
        for i in range(1, n - m + 1):
            old = (ord(haystack[i - 1]) - ord('a')) * highest_pow
            new = ord(haystack[i + m - 1]) - ord('a')
            h_hash = ((h_hash - old) * BASE + new) % MOD
            if h_hash == n_hash:
                if haystack[i: i+m] == needle:
                    return i
        return -1