class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle)

        # h, n = len(haystack), len(needle)
        # for i in range(h - n + 1):
        #     if haystack[i:i+n] == needle:
        #         return i
        # return -1

        n, m = len(haystack), len(needle)
        if not needle or m > n: return -1
        BASE = 26
        MOD = 10**9 + 7
        highest_pow = pow(BASE, m - 1, MOD)
        print(highest_pow)
        needle_hash = 0
        window_hash = 0
        for i in range(m):
            needle_hash = (needle_hash * BASE + (ord(needle[i]) - ord('a'))) % MOD
            window_hash = (window_hash * BASE + (ord(haystack[i]) - ord('a'))) % MOD
        for i in range(n - m + 1):
            if window_hash == needle_hash:
                if haystack[i : i + m] == needle:
                    return i
            if i < n - m:
                leading = ord(haystack[i]) - ord('a')
                new = ord(haystack[i + m]) - ord('a')
                window_hash = (window_hash - (leading * highest_pow)) % MOD
                window_hash = (window_hash * BASE + new) % MOD
        return -1