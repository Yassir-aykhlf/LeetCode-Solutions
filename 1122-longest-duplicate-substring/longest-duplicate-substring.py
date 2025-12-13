class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def check(n):
            seen = {}
            MOD = 10**9 + 7
            BASE = 26
            highest_pow = pow(BASE, n - 1, MOD)
            r_hash = 0
            for i in range(n):
                r_hash = (r_hash * BASE + (ord(s[i]) - ord('a'))) % MOD
            seen[r_hash] = 0
            for i in range(1, len(s) - n + 1):
                old = (ord(s[i - 1]) - ord('a'))
                new = (ord(s[i + n - 1]) - ord('a'))
                r_hash = ((r_hash - old * highest_pow) * BASE + new) % MOD
                if r_hash in seen:
                    prev_i = seen[r_hash]
                    if s[prev_i : prev_i + n] == s[i : i + n]:
                        return i
                else:
                    seen[r_hash] = i
            return -1
        
        l, r = 1, len(s) - 1
        best_start = -1
        best_len = 0
        while l <= r:
            mid = (l + r) // 2
            index = check(mid)
            if index != -1:
                best_start = index
                best_len = mid
                l = mid + 1
            else:
                r = mid - 1
        return s[best_start: best_start + best_len] if best_start != -1 else ""