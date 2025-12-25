class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def check(n):
            seen = {}
            hash1 = 0
            base, mod = 31, 10**9 + 7
            highest_pow = pow(base, n - 1, mod)
            for i in range(n):
                hash1 = (hash1 * base + ord(s[i])) % mod
            seen[hash1] = 0
            for i in range(1, len(s) - n + 1):
                new = (ord(s[i + n - 1])) % mod
                old = (ord(s[i - 1]) * highest_pow) % mod
                hash1 = ((hash1 - old) * base + new) % mod
                if hash1 in seen:
                    if s[seen[hash1] : seen[hash1] + n] == s[i : i + n]:
                        return i
                seen[hash1] = i
            return -1

        l, r = 0, len(s) - 1
        index, length = -1, 0
        while l <= r:
            mid = (l + r) // 2
            ans = check(mid)
            if ans != -1:
                index = ans
                length = mid
                l = mid + 1
            else:
                r = mid - 1
        return s[index : index + length] if index != -1 else ""