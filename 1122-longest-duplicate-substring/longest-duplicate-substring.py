class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def search(n):
            seen = {}
            base, mod = 31, 10 ** 9 + 7
            highest_pow = pow(base, n - 1, mod)
            hash_ = 0
            for i in range(n):
                hash_ = (hash_ * base + ord(s[i])) % mod
            seen[hash_] = 0
            for i in range(1, len(s) - n + 1):
                new = ord(s[i + n - 1])
                old = ord(s[i - 1])
                hash_ = ((hash_ - old * highest_pow) * base + new) % mod
                if hash_ in seen and s[seen[hash_] : seen[hash_] + n] == s[i:i + n]:
                    return seen[hash_]
                seen[hash_] = i
            return -1
        lo, hi = 0, len(s)
        best_i, best_len = -1 , 0
        while lo <= hi:
            n = (lo + hi) // 2
            index = search(n)
            if index != -1:
                best_i = index
                best_len = n
                lo = n + 1
            else:
                hi = n - 1
        return s[best_i : best_i + best_len] if best_i != -1 else ""