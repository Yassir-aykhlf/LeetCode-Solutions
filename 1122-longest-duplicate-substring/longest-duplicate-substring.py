class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def check(n):
            base = 26
            mod = 2**63 - 7
            highest_pow = pow(base, n - 1, mod)
            r_hash = 0
            seen = set()
            for i in range(n):
                r_hash = (r_hash * base + (ord(s[i]) - ord('a'))) % mod
            seen.add(r_hash)
            for i in range(1, len(s) - n + 1):
                old = ord(s[i - 1]) - ord('a')
                new = ord(s[i + n - 1]) - ord('a')
                r_hash = (((r_hash - (old * highest_pow)) * base) + new) % mod
                if r_hash in seen:
                    return i
                seen.add(r_hash)
            return -1
        
        l, r = 0, len(s) - 1
        best_len = 0
        best_i = -1
        while l <= r:
            mid = (l + r) // 2
            index = check(mid)
            if index != -1:
                best_i = index
                best_len = mid
                l = mid + 1
            else:
                r = mid - 1
        return s[best_i : best_i + best_len] if best_i != -1 else ""