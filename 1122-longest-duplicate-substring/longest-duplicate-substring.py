class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def dup_exist(pot_len):
            seen = {}
            MOD = 10 ** 9 + 7
            BASE = 31
            highest_pow = pow(BASE, pot_len - 1, MOD)
            hash = 0
            for i in range(pot_len):
                hash = (hash * BASE + ord(s[i])) % MOD
            seen[hash] = 0
            for i in range(pot_len, len(s)):
                old_val = ord(s[i - pot_len]) * highest_pow
                new_val = ord(s[i]) 
                hash = ((hash - old_val) * BASE + ord(s[i])) % MOD
                if hash in seen and s[seen[hash]: seen[hash] + pot_len] == s[i - pot_len + 1: i + 1]:
                    return i - pot_len + 1
                seen[hash] = i - pot_len + 1
            return -1
        lo, hi = 0, len(s)
        best_len = hi
        best_idx = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            idx = dup_exist(mid)
            if idx != -1:
                best_len = mid
                best_idx = idx
                lo = mid + 1
            else:
                hi = mid - 1
        return s[best_idx : best_idx + best_len] if best_idx != -1 else ""