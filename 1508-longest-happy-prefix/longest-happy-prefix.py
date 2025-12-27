class Solution:
    def longestPrefix(self, s: str) -> str:
        max_len = 0
        p_hash, s_hash = 0, 0
        base, mod, power = 31, 10**9+7, 1
        for i in range(len(s) - 1):
            p_hash = (p_hash * base + ord(s[i])) % mod
            s_hash = (s_hash + power * ord(s[len(s) - 1 - i])) % mod
            power = power * base % mod
            if p_hash == s_hash:
                max_len = max(max_len, i + 1)
        return s[:max_len]