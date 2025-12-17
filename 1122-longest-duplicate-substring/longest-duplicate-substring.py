class Solution:
    def check(self, s: str, n: int) -> int:
        mod = 10**9 + 7
        base = 31
        highest_pow = pow(base, n - 1, mod)
        r_hash = 0
        seen = {}
        for i in range(n):
            r_hash = (r_hash * base + ord(s[i])) % mod
        seen[r_hash] = 0
        for i in range(1, len(s) - n + 1):
            old = (ord(s[i - 1]) * highest_pow) % mod
            new = ord(s[i + n - 1])
            r_hash = ((r_hash - old) * base + new) % mod
            if r_hash in seen and s[seen[r_hash] : seen[r_hash] + n] == s[i : i + n]:
                return i
            seen[r_hash] = i
        return -1
    def longestDupSubstring(self, s: str) -> str:
        best_index = -1
        best_len = 0
        low, high = 0, len(s) - 1
        while low <= high:
            mid = (low + high) // 2
            index = self.check(s, mid)
            if index != -1:
                best_len = mid
                best_index = index
                low = mid + 1
            else:
                high = mid - 1
        return s[best_index : best_index + best_len] if best_index != -1 else ""