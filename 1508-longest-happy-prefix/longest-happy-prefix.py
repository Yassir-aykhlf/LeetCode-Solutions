class Solution:
    def longestPrefix(self, s: str) -> str:
        mod = 10**9 + 7
        base = 31
        power = 1
        prefix_hash = 0
        suffix_hash = 0
        longest_index = 0
        for i in range(len(s) - 1):
            p_old = ord(s[i]) - ord('a') + 1
            prefix_hash = (prefix_hash * base + p_old) % mod
            s_old = ord(s[len(s) - 1 - i]) - ord('a') + 1
            suffix_hash = (suffix_hash + s_old * power) % mod
            power = (power *base) % mod
            if prefix_hash == suffix_hash:
                longest_index = i + 1
        return s[:longest_index]