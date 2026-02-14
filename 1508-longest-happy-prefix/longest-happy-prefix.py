class Solution:
    def longestPrefix(self, s: str) -> str:
        p_hash = 0
        s_hash = 0
        BASE = 31
        MOD = 10 ** 9 + 7
        power = 1
        max_len = 0
        n = len(s)
        for i in range(n - 1):
            p_hash = (p_hash * BASE + ord(s[i])) % MOD
            s_hash = (s_hash + ord(s[n - i - 1]) * power) % MOD
            power = power * BASE % MOD
            if p_hash == s_hash:
                max_len = i + 1
        return s[:max_len]