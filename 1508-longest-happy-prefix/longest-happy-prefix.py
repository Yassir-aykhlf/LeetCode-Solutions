class Solution:
    def longestPrefix(self, s: str) -> str:
        mod = 10**9 + 7
        base = 31
        power = 1
        res = 0
        r_hash, l_hash = 0, 0
        for i in range(len(s) - 1):
            r_hash = (r_hash * base + ord(s[i])) % mod
            l_hash = (l_hash + ord(s[len(s) - 1 - i]) * power) % mod
            power = (power * base) % mod
            if r_hash == l_hash:
                res = i + 1
        return s[:res] if res else ""