class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def check(length):
            seen = set()
            current_hash = 0
            BASE = 26
            MOD = 2**63 - 1
            highest_pow = pow(BASE, length - 1, MOD)
            for i in range(length):
                current_hash = (current_hash * BASE + (ord(s[i]) - ord('a'))) % MOD
            seen.add(current_hash)
            for i in range(1, len(s) - length + 1):
                prev = ord(s[i - 1]) - ord('a')
                new  = ord(s[i + length - 1]) - ord('a')
                current_hash = (current_hash - prev * highest_pow) % MOD
                current_hash = (current_hash * BASE + new) % MOD
                if current_hash in seen:
                    return i
                seen.add(current_hash)
            return -1
        low, high = 1, len(s) - 1
        best_start = -1
        while low <= high:
            mid = (low + high) // 2
            found = check(mid)
            if found != -1:
                best_start = found
                low = mid + 1
            else:
                high = mid - 1
        return s[best_start : best_start + (low - 1)] if best_start != -1 else ""