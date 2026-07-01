class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            a, b = i, i
            while a >= 0 and b < len(s) and s[a] == s[b]:
                count += 1
                a -= 1
                b += 1
            a, b = i, i + 1
            while a >= 0 and b < len(s) and s[a] == s[b]:
                count += 1
                a -= 1
                b += 1
        return count