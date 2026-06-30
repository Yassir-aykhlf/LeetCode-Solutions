class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            a, b = i, i
            while a >= 0 and b < len(s) and s[a] == s[b]:
                res += 1
                a -= 1
                b += 1
            a, b = i, i + 1
            while a >= 0 and b < len(s) and s[a] == s[b]:
                res += 1
                a -= 1
                b += 1
        return res