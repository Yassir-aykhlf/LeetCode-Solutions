class Solution:
    def longestPrefix(self, s: str) -> str:
        mod = 10 ** 9 + 7
        base = 31
        _pow = 1
        prefix_hash = 0
        suffix_hash = 0
        max_len = 0
        for i in range(len(s) - 1):
            prefix_hash = (prefix_hash * base + ord(s[i])) % mod
            suffix_hash = (suffix_hash + ord(s[len(s) - i - 1]) * _pow) % mod
            _pow = (_pow * base) % mod
            if prefix_hash == suffix_hash:
                max_len = i + 1
        return s[:max_len]